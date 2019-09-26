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
    def set_job_step_value(proc_cont):
        """
        . 设置v_job_step的值
        . 将写死的job_step,改为变量
        """
        error_bat_log_value = "VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,'-1',V_JOB_NAME"
        bat_log_value = "VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,"
        proc_cont_last_half = proc_cont.split(bat_log_value)[1]
        job_step = proc_cont_last_half.split(",")[0]

        if proc_cont.find(error_bat_log_value) > -1:
            proc_cont = proc_cont.replace('-1', "V_JOB_STEP")
        else:
            # add line of v_job_step
            # VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,'19',V_JOB_NAME
            v_job_step_line = "V_JOB_STEP:={};\n".format(int(eval(job_step)))
            proc_cont = proc_cont.replace("INSERT INTO", v_job_step_line + "INSERT INTO")

            # replace hard code value with v_job_step
            proc_cont = proc_cont.replace(bat_log_value + job_step, bat_log_value + "V_JOB_STEP")
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
        proc_cont = self.set_job_step_value(proc_cont)
        # 4.查找是否spend time已经减一了，如果有就修正
        proc_cont = self.spend_time_value_adjust(proc_cont)

        return proc_cont

    # @staticmethod
    # def add_report_log(proc_cont:str)-> str:
    #    """添加 bat_report_log 登记
    #    TODO两个timestamp之间不是很好的划分，
    #    """
    #    pass

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
    def is_log_exists_between_timestamp(proc_cont_between_commmit) -> bool:
        return proc_cont_between_commmit.find("BAT_REPORT_LOG") > -1

    def modify_procedure_header(self, proc_cont: str) -> str:
        """修改存储过程头部部分
        """
        proc_cont = self.add_header_log(proc_cont)
        # not find then add 
        if proc_cont.find("V_JOB_STEP") == -1:
            proc_cont = self.declare_job_step(proc_cont)
        return proc_cont

    def modify_procedure_between_timestamp(self, proc_cont: str):
        """修改存储过程两个timestamp之间的部分
            TODO 如果两个;之间没有timestamp,会导致无法添加日志
        """
        if self.is_log_exists_between_timestamp(proc_cont):
            return self.modify_report_log(proc_cont)
        # else:
        #    return self.add_report_log(proc_cont)
        return proc_cont

    def modify_procedure_log(self):
        """主入口"""
        # read proc_cont
        procedure = self.__procedure
        proc_cont = procedure.read_proc_cont()
        proc_cont_head, proc_cont_main = proc_cont.split("IF I_RUN_DATE IS NULL THEN\n")
        proc_cont_head = self.modify_procedure_header(proc_cont_head)

        split_str = "CURRENT_TIMESTAMP"
        proc_cont_main_list = proc_cont_main.split(split_str)
        for ind in range(0, len(proc_cont_main_list)):
            proc_cont_main_list[ind] = self.modify_procedure_between_timestamp(
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
