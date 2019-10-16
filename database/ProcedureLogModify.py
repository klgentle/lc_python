"""
    存储过程日志修改
     1. 添加主日志
     2. job_step 写死的，改为变量
     3. 添加 bat_report_log 登记
     4. 日志编号在最后统一重写
"""


import os
import re
import sys
import time
import logging

# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from database.Procedure import Procedure

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class ProcedureLogModify(object):
    """
    agr:proc_name
    """

    def __init__(self, proc_name: str):
        self.__procedure = Procedure(proc_name)

    @staticmethod
    def declare_variable(variable_name: str, variable_type: str) -> str:
        """根据名称与类型，申明变量
        """
        return "  {0}\t\t{1};\n".format(variable_name, variable_type)

    def declare_job_step(self, proc_cont: str) -> str:
        "add declare before BEGIN"
        job_step_variable = self.declare_variable("V_JOB_STEP", "NUMBER")
        # return proc_cont.replace("BEGIN", job_step_variable + "BEGIN")
        return re.sub(
            r"BEGIN", job_step_variable + "BEGIN", proc_cont, flags=re.IGNORECASE
        )

    @staticmethod
    def set_job_step_value_and_modify_insert(proc_cont):
        """
        . 设置v_job_step的值
        . 将写死的job_step,改为变量
        """
        error_bat_log_pattern = r"V_DEAL_DATE,\n?\s*'?(-?\d+)'?,\n?\s*V_JOB_NAME"
        match = re.search(error_bat_log_pattern, proc_cont, flags=re.IGNORECASE)
        try:
            job_step = match.group(1)
        except:
            logging.error("proc_cont: %s" % proc_cont)
            return proc_cont

        if match and job_step == "-1":
            proc_cont = re.sub(
                r"V_DEAL_DATE\s*,\n?\s*'?-1'?",
                "V_DEAL_DATE,V_JOB_STEP",
                proc_cont,
                flags=re.IGNORECASE,
            )
        else:
            # add line of v_job_step
            v_job_step_line = "V_JOB_STEP:={};\n".format(job_step)
            batch_insert_pattern = r"INSERT\s+INTO\s+BAT_REPORT_LOG"
            proc_cont = re.sub(
                batch_insert_pattern,
                v_job_step_line + r"INSERT INTO BAT_REPORT_LOG",
                proc_cont,
                flags=re.IGNORECASE,
            )

            # replace hard code value with v_job_step
            bat_log_value = r"V_DEAL_DATE,\n?\s*'?{}'?".format(job_step)
            proc_cont = re.sub(
                bat_log_value, "V_DEAL_DATE,V_JOB_STEP", proc_cont, flags=re.IGNORECASE
            )
        return proc_cont

    @staticmethod
    def spend_time_value_adjust(proc_cont: str) -> str:
        """查找是否spend time已经减一了，如果有就修正"""
        pattern = r"V_ST_TIME\s*-\s*1"
        if re.search(pattern, proc_cont, flags=re.IGNORECASE):
            proc_cont = re.sub(pattern, "V_ST_TIME", proc_cont, flags=re.IGNORECASE)
        return proc_cont

    def modify_report_log(self, proc_cont: str) -> str:
        """修改 bat_report_log 登记
        """
        logging.info("修改 bat_report_log 登记")
        if self.is_log_exists_and_need_modify(proc_cont):
            proc_cont = self.set_job_step_value_and_modify_insert(proc_cont)
        proc_cont = self.spend_time_value_adjust(proc_cont)

        return proc_cont

    @staticmethod
    def is_log_exists_and_need_modify(proc_cont_between_log) -> bool:
        proc_cont_list = proc_cont_between_log.split("BAT_SERIAL_NO.NEXTVAL,")
        # 如果存在VALUES(BAT_SERIAL_NO.NEXTVAL,则list长度会大于一
        if len(proc_cont_list) > 1 and not proc_cont_list[1].upper().replace(
            "\n", ""
        ).replace(" ", "").strip().startswith("V_DEAL_DATE,V_JOB_STEP,V_JOB_NAME"):
            return True
        return False

    def modify_procedure_header(self, proc_cont: str) -> str:
        """修改存储过程头部部分
        """
        proc_cont = self.__procedure.add_header_log(proc_cont)
        # not find then add
        if not re.search("V_JOB_STEP", proc_cont, flags=re.IGNORECASE):
            proc_cont = self.declare_job_step(proc_cont)
        return proc_cont

    @staticmethod
    def bat_log_template():
        bat_report_log = """COMMIT;

V_END_TIME:=CURRENT_TIMESTAMP ;    --处理结束时间
V_SPEND_TIME:=ROUND(TO_NUMBER(TO_DATE(TO_CHAR(V_END_TIME,'YYYY-MM-DD HH24:MI:SS') ,'YYYY-MM-DD HH24:MI:SS')
 -TO_DATE(TO_CHAR(V_ST_TIME,'YYYY-MM-DD HH24:MI:SS') ,'YYYY-MM-DD HH24:MI:SS')) * 24 * 60 * 60);----执行时间

V_JOB_STEP:=1;
INSERT INTO BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)
VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,V_JOB_STEP,V_JOB_NAME,V_SPEND_TIME,V_ERR_MSG,V_JOB_ID,V_JOB_STEP||'结束...');
COMMIT;\n
"""
        return bat_report_log

    def add_report_log(self, content: str) -> str:
        target_str = "INSERT INTO"
        content_list = content.split(target_str)
        # content_list =['开始处理...', 'RPT_CIF032_D_1...', 'RPT_CIF032_D_2...', 'BAT_REPORT_LOG']
        # 从第二个至倒数第二都要加日志
        keep_list = content_list[0:1]
        to_add_log_list = content_list[1:]
        # the last one no need
        log_content_list = [" "] * len(to_add_log_list)
        logging.info("add report log")
        for i in range(0, len(to_add_log_list) - 2):
            sql = "".join([to_add_log_list[i], self.bat_log_template()])
            log_content_list[i] = sql

        # last one is bat log, no need to modify
        log_content_list[-2:] = to_add_log_list[-2:]
        keep_list.extend(log_content_list)
        return target_str.join(keep_list)

    def modify_log_register(self, proc_cont: str):
        """修改存储过程两个report_log之间的部分
        """
        proc_cont = self.modify_report_log(proc_cont)
        # TODO test
        if proc_cont.count("INSERT INTO") > 2:
            proc_cont = self.add_report_log(proc_cont)
        return proc_cont

    def reset_job_step_value(self):
        """modify all job_step value after log add and modify
        """
        procedure = self.__procedure
        proc_cont = procedure.read_proc_cont()
        pattern = r"V_JOB_STEP\s*:=\s*\d+;"
        job_step_value_list = re.findall(pattern, proc_cont)
        job_step_num = len(job_step_value_list)
        standard_job_value_list = [
            "V_JOB_STEP:={};".format(i) for i in range(job_step_num)
        ]
        if job_step_value_list != standard_job_value_list:
            logging.info("job_step value reset")
            proc_cont_list = re.split(pattern, proc_cont)
            # from the second to the end, add split pattern
            for i in range(1, len(proc_cont_list)):
                proc_cont_list[i] = "\n".join(
                    [standard_job_value_list[i - 1], proc_cont_list[i]]
                )

            # write procedure file
            procedure.write_procedure("".join(proc_cont_list))

    def main(self):
        """主入口
        """
        # read proc_cont
        procedure = self.__procedure
        proc_cont = procedure.read_proc_cont()
        proc_cont_head, proc_cont_main = re.split(
            r"IF\s+I_RUN_DATE\s+IS\s+NULL", proc_cont, flags=re.IGNORECASE
        )
        # TODO only write log after modify
        proc_cont_head = self.modify_procedure_header(proc_cont_head)

        main_split_str = r"V_JOB_ID"
        proc_cont_main_list = re.split(
            main_split_str, proc_cont_main, flags=re.IGNORECASE
        )

        for ind in range(0, len(proc_cont_main_list)):
            proc_cont_main_list[ind] = self.modify_log_register(
                proc_cont_main_list[ind]
            )

        # write procedure file
        procedure.write_procedure(
            proc_cont_head
            + "IF I_RUN_DATE IS NULL"
            + main_split_str.join(proc_cont_main_list)
        )
        self.reset_job_step_value()
        logging.info("日志修改完成!")


if __name__ == "__main__":
    obj = ProcedureLogModify("p_rpt_cif033")
    obj.main()
