from Procedure import Procedure
import time


class ProcedudreLogModify(object):
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
                "INSERT INTO", v_job_step_line + "INSERT INTO"
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
        header_log = "  V2.0  {0} dongjian    log modify\n".format(date_str)
        log_end = "+===================="
        return proc_cont.replace(log_end, header_log + log_end)

    @staticmethod
    def is_log_exists_and_need_modify(proc_cont_between_log) -> bool:
        proc_cont_list = proc_cont_between_log.split("VALUES(BAT_SERIAL_NO.NEXTVAL,")
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
        bat_report_log = """
COMMIT;

V_END_TIME:=CURRENT_TIMESTAMP ;    --处理结束时间
V_SPEND_TIME:=ROUND(TO_NUMBER(TO_DATE(TO_CHAR(V_END_TIME,'YYYY-MM-DD HH24:MI:SS') ,'YYYY-MM-DD HH24:MI:SS')
 -TO_DATE(TO_CHAR(V_ST_TIME,'YYYY-MM-DD HH24:MI:SS') ,'YYYY-MM-DD HH24:MI:SS')) * 24 * 60 * 60);----执行时间

V_JOB_STEP:=1;
INSERT INTO BAT_REPORT_LOG(DEAL_SERIAL_NO,DEAL_DATE,JOB_STEP,JOB_NAME,SPEND_TIME,REMARK,JOB_ID,JOB_STATE)
VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,V_JOB_STEP,V_JOB_NAME,V_SPEND_TIME,V_ERR_MSG,V_JOB_ID,'结束处理...');
COMMIT;
        """
        return bat_report_log

    @staticmethod
    def add_report_log(content: str, target_str: str) -> str:
        content_list = content.split(target_str)
        # s2 =['d', ' b ', ' c ', ' css']
        # 从第二个至最后都要加日志
        # TODO 日志编号 编号可以在最后统一重写一遍
        to_add_log_list = content_list[2:]
        # the last one no need
        log_content_list = [" "] * len(to_add_log_list)
        for i in range(0, len(to_add_log_list) - 1):
            sql = to_add_log_list[i] + self.bat_log_template()
            log_content_list[i] = sql

        log_content_list[-1] = to_add_log_list[-1]
        return target_str.join(content_list[0:2] + log_content_list)

    def modify_procedure_between_report_log(self, proc_cont: str):
        """修改存储过程两个report_log之间的部分
            TODO 如果两个;之间没有report_log,会导致无法添加日志
        """
        if self.is_log_exists_and_need_modify(proc_cont):
            proc_cont = self.modify_report_log(proc_cont)
        # TODO test
        # if proc_cont.count('INSERT INTO') >2:
        #    proc_cont =  self.add_report_log(proc_cont)
        return proc_cont

    def modify_procedure_log(self):
        """主入口"""
        # read proc_cont
        procedure = self.__procedure
        proc_cont = procedure.read_proc_cont()
        proc_cont_head, proc_cont_main = proc_cont.split("IF I_RUN_DATE IS NULL THEN\n")
        proc_cont_head = self.modify_procedure_header(proc_cont_head)

        split_str = "V_JOB_ID"
        proc_cont_main_list = proc_cont_main.split(split_str)
        for ind in range(0, len(proc_cont_main_list)):
            proc_cont_main_list[ind] = self.modify_procedure_between_report_log(
                proc_cont_main_list[ind]
            )

        # write procedure file
        procedure.write_procedure(
            proc_cont_head
            + "IF I_RUN_DATE IS NULL THEN\n"
            + split_str.join(proc_cont_main_list)
        )
        print("日志修改完成!")


if __name__ == "__main__":
    obj = ProcedudreLogModify("p_rpt_cif032")
    obj.modify_procedure_log()
