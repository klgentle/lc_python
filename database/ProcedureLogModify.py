import os
import re
import sys
import time

# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from database.Procedure import Procedure


class ProcedureLogModify(object):
    """
    存储过程日志修改
     添加主日志，如：  V1.0   20180515 HASON       1.ADD SCHEMA
     job_step 写死的，改为变量
     添加 bat_report_log 登记

    TODO add log, 修改存储过程划分:
    按 V spend time分块
两个日志之间不能有两个以上的insert 否则要写日志，3个insert 增加一个日志，4个insert增加两个。
日志写在第二个insert前，
    改日志最好是按行读取，
    # TODO joshua 日志编号 编号可以在最后统一重写一遍
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
        return proc_cont.replace("BEGIN", job_step_variable + "BEGIN")

    @staticmethod
    def set_job_step_value_and_modify_insert(proc_cont):
        """
        . 设置v_job_step的值
        . 将写死的job_step,改为变量
        """
        error_bat_log_value = (
            "VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,'-1',V_JOB_NAME"
        )
        bat_log_value = "VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,"
        proc_cont_last_half = proc_cont.split(bat_log_value)[1]
        job_step = proc_cont_last_half.split(",")[0]

        if proc_cont.find(error_bat_log_value) > -1:
            proc_cont = proc_cont.replace("-1", "V_JOB_STEP")
        else:
            # add line of v_job_step
            # VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,'19',V_JOB_NAME
            v_job_step_line = "V_JOB_STEP:={};\n".format(int(eval(job_step)))
            proc_cont = proc_cont.replace(
                "INSERT INTO BAT_REPORT_LOG", v_job_step_line + "INSERT INTO BAT_REPORT_LOG"
            )

            # replace hard code value with v_job_step
            proc_cont = proc_cont.replace(
                bat_log_value + job_step, bat_log_value + "V_JOB_STEP"
            )
        return proc_cont

    @staticmethod
    def spend_time_value_adjust(proc_cont: str) -> str:
        """查找是否spend time已经减一了，如果有就修正"""
        if proc_cont.find("V_ST_TIME-1") > -1:
            return proc_cont.replace("V_ST_TIME-1", "V_ST_TIME")
        return proc_cont

    def modify_report_log(self, proc_cont: str) -> str:
        """修改 bat_report_log 登记
        """
        print("修改 bat_report_log 登记")
        proc_cont = self.set_job_step_value_and_modify_insert(proc_cont)
        # 4.查找是否spend time已经减一了，如果有就修正
        proc_cont = self.spend_time_value_adjust(proc_cont)

        return proc_cont

    @staticmethod
    def add_header_log(proc_cont: str) -> str:
        """添加起始位置的log登记
        如：  V1.0   20180515 HASON       1.ADD SCHEMA
        """
        date_str = time.strftime("%Y%m%d", time.localtime())
        header_log = "  V2.0  {0} \tdongjian    log modify\n".format(date_str)
        log_end = "+===================="
        return proc_cont.replace(log_end, header_log + log_end)

    @staticmethod
    def is_log_exists_and_need_modify(proc_cont_between_log) -> bool:
        proc_cont_list = proc_cont_between_log.split(
            "VALUES(BAT_SERIAL_NO.NEXTVAL,")
        # 如果存在VALUES(BAT_SERIAL_NO.NEXTVAL,则list长度会大于一
        if len(proc_cont_list) > 1 and not proc_cont_list[1].strip().startswith(
            "V_DEAL_DATE,V_JOB_STEP,V_JOB_NAME"
        ):
            return True
        return False

    def modify_procedure_header(self, proc_cont: str) -> str:
        """修改存储过程头部部分
        """
        proc_cont = self.add_header_log(proc_cont)
        # not find then add
        if proc_cont.find("V_JOB_STEP") == -1:
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
        for i in range(0, len(to_add_log_list) - 2):
            print('add_report_log')
            sql = "".join([to_add_log_list[i], self.bat_log_template()])
            log_content_list[i] = sql

        # last one is bat log, no need to modify 
        log_content_list[-2:] = to_add_log_list[-2:]
        keep_list.extend(log_content_list)
        return target_str.join(keep_list)

    def modify_log_register(self, proc_cont: str):
        """修改存储过程两个report_log之间的部分
        """
        if self.is_log_exists_and_need_modify(proc_cont):
            proc_cont = self.modify_report_log(proc_cont)
        # TODO test
        if proc_cont.count('INSERT INTO') > 2:
            proc_cont = self.add_report_log(proc_cont)
        return proc_cont

    def reset_job_step_value(self):
        """modify all job_step value after log add and modify
        """
        procedure = self.__procedure
        proc_cont = procedure.read_proc_cont()
        pattern = r"V_JOB_STEP\s*:=\s*\d+;"
        job_step_value_list = re.findall(pattern,proc_cont)
        job_step_num = len(job_step_value_list)
        standard_job_value_list = ['V_JOB_STEP:={};'.format(i) for i in range(job_step_num)]
        if job_step_value_list != standard_job_value_list:
            print("job_step value reset")
            proc_cont_list = re.split(pattern, proc_cont)
            # from the second to the end, add split pattern
            for i in range(1, len(proc_cont_list)):
                proc_cont_list[i] = "".join([standard_job_value_list[i-1], proc_cont_list[i]])

        # write procedure file
        procedure.write_procedure("".join(proc_cont_list))

    def main(self):
        """主入口"""
        # read proc_cont
        procedure = self.__procedure
        proc_cont = procedure.read_proc_cont()
        proc_cont_head, proc_cont_main = proc_cont.split(
            "IF I_RUN_DATE IS NULL THEN")
        proc_cont_head = self.modify_procedure_header(proc_cont_head)

        main_split_str = "V_JOB_ID"
        proc_cont_main_list = proc_cont_main.split(main_split_str)

        for ind in range(0, len(proc_cont_main_list)):
            proc_cont_main_list[ind] = self.modify_log_register(
                proc_cont_main_list[ind]
            )

        # write procedure file
        procedure.write_procedure(
            proc_cont_head
            + "IF I_RUN_DATE IS NULL THEN"
            + main_split_str.join(proc_cont_main_list)
        )
        self.reset_job_step_value()
        print("日志修改完成!")


if __name__ == "__main__":
    obj = ProcedureLogModify("p_rpt_cif032")
    #obj.main()
    #obj.add_report_log()
    obj.reset_job_step_value()