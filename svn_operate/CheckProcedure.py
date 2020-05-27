import re
import os
import platform
from config_default import configs


class CheckProcedure(object):
    def __init__(self):
        if platform.uname().system == "Windows":
            self.procedure_path = configs.get("path").get("win_svn_procedure_path")
        else:
            self.procedure_path = configs.get("path").get("svn_procedure_path")

    def find_procedure_modify(self):
        os.chdir(self.procedure_path)
        svn_st_list = os.popen("svn st").read().strip("\n").split("\n")
        # 取 add
        svn_add_filter = filter(lambda x: x.startswith("? "), svn_st_list)
        # 取 modify
        svn_modify_filter = filter(lambda x: x.startswith("M "), svn_st_list)
        svn_list = list(
            map(
                lambda x: x.strip("?       ").strip("M       "),
                list(svn_add_filter) + list(svn_modify_filter),
            )
        )
        #print(svn_list)
        return svn_list

    def check_procedures(self): -> bool
        """
        循环检测
        """
        procedure_list = self.find_procedure_modify()
        check_pass = True
        for prcedure in procedure_list:
            if not self.check_procedure(prcedure):
                check_pass = False
        return check_pass

    def check_procedure(self, procedure: str): -> bool
        """
        检测一个存储过程
        """
        if self.is_date_hard_code(procedure):
            print(
                "Warning: {} date is hard code, please check! __________________".format(
                    procedure
                )
            )
            return False
        return True

    def is_date_hard_code(self, procedure: str) -> bool:
        """
        检查是否有将日期写死，如将v_deal_date 写date'20...'
        """
        with open(os.path.join(self.procedure_path, procedure), "r", encoding="utf-8") as f:
            proc_cont = f.read()
            if re.search("date'20", proc_cont, flags=re.IGNORECASE):
                return True

        return False


if __name__ == "__main__":
    a = CheckProcedure()
    # tests
    # assert a.is_date_hard_code("p_rpt_lon800_2.sql") is False
    # a.check_procedure("p_rpt_lon800_2.sql")
    #a.find_procedure_modify()
    a.check_procedures()
