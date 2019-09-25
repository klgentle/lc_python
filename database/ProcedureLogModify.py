from Procedure import Procedure
import time


class ProcedudreLogModify(object):
    """
    存储过程日志修改
     添加主日志，如：  V1.0   20180515 HASON       1.ADD SCHEMA
     job_step 写死的，改为变量
     添加 bat_report_log 登记
    """

    def __init__(self, proc_name:str):
        self.__procedure = Procedure(proc_name)


    def is_job_step_exists(self):
        """检查是否存在v_job_step"""
        # TODO
        proc_cont = ""
        if proc_cont.find('V_JOB_STEP') > -1:
            return True
        return False

    @staticmethod
    def declare_variable(variable_name:str, variable_type:str) -> str:
        """根据名称与类型，申明变量
        """
        return "  {0}\t\t{1};\n".format(variable_name,variable_type)

    def declare_job_step(self, proc_cont:str) -> str:
        "add declare before BEGIN"
        job_step_variable = self.declare_variable('V_JOB_STEP',"NUMBER")
        return proc_cont.replace('BEGIN', job_step_variable + 'BEGIN')

    @staticmethod
    def set_job_step_value(proc_cont):
        """
        . 设置v_job_step的值
        . 将写死的job_step,改为变量
        """
        # add line of v_job_step
        #VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,'19',V_JOB_NAME
        bat_log_value = "VALUES(BAT_SERIAL_NO.NEXTVAL, V_DEAL_DATE,"
        proc_cont_last_half = proc_cont.split(bat_log_value)[1]
        job_step = proc_cont_last_half.split(',')[0]
        v_job_step_line = "V_JOB_STEP:={};\n".format(int(eval(job_step)))
        proc_cont = proc_cont.replace("INSERT INTO", v_job_step_line + "INSERT INTO") 
        
        # replace hard code value with v_job_step
        # TODO
        #print(f"proc_cont_head_changed:{proc_cont_head_changed}")
        return proc_cont.replace(bat_log_value+job_step,bat_log_value+'V_JOB_STEP') 

    @staticmethod
    def spend_time_value_adjust(proc_cont:str)-> str:
        """查找是否spend time已经减一了，如果有就修正"""
        return proc_cont.replace('V_ST_TIME-1','V_ST_TIME')

    def modify_report_log(self, proc_cont:str)-> str:
        """修改 bat_report_log 登记
        """
        print('修改 bat_report_log 登记')
        proc_cont = self.set_job_step_value(proc_cont)
        #4.查找是否spend time已经减一了，如果有就修正
        if proc_cont.find('V_ST_TIME-1') > -1:
            proc_cont = self.spend_time_value_adjust(proc_cont)

        return proc_cont

    #@staticmethod
    #def add_report_log(proc_cont:str)-> str:
    #    """添加 bat_report_log 登记
    #    TODO两个commit之间不是很好的划分，
    #    """
    #    pass

    @staticmethod
    def add_header_log(proc_cont:str)-> str:
        """添加起始位置的log登记
        如：  V1.0   20180515 HASON       1.ADD SCHEMA
        """
        date_str = time.strftime("%Y%m%d", time.localtime())
        header_log = "  V2.0  {0} dongjian    log modify\n".format(date_str)
        log_end = "+===================="
        return proc_cont.replace(log_end, header_log + log_end)

    @staticmethod
    def is_log_exists_between_commit(proc_cont_between_commmit) -> bool:
        return proc_cont_between_commmit.find('BAT_REPORT_LOG') > -1

    def modify_procedure_header(self, proc_cont:str)->str:
        """修改存储过程头部部分
        """
        proc_cont = self.add_header_log(proc_cont)
        if not self.is_job_step_exists():
            proc_cont = self.declare_job_step(proc_cont)
        return proc_cont

    def modify_procedure_between_commit(self, proc_cont:str):
        """修改存储过程两个commit之间的部分
            TODO 如果两个;之间没有commit,会导致无法添加日志
        """
        if self.is_log_exists_between_commit(proc_cont):
            return self.modify_report_log(proc_cont)
        #else:
        #    return self.add_report_log(proc_cont)
        return proc_cont

    def modify_procedure_log(self):
        """主入口"""
        # read proc_cont
        procedure = self.__procedure
        proc_cont = procedure.read_proc_cont()
        proc_cont_list = proc_cont.split("COMMIT;\n")
        proc_cont_list[0] = self.modify_procedure_header(proc_cont_list[0])
        for ind in range(0,len(proc_cont_list)):
            proc_cont_list[ind] = self.modify_procedure_between_commit(proc_cont_list[ind])

        # write procedure file
        procedure.write_procedure("COMMIT;\n".join(proc_cont_list))
        print("日志修改完成!")


if __name__ == "__main__":
    obj = ProcedudreLogModify('p_rpt_cif032')
    obj.modify_procedure_log()