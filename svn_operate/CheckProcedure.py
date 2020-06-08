import re
import os
import platform
from config_default import configs


class CheckProcedure(object):
    def __init__(self):
        # 不需要检查的程序清单
        self.white_list = [
            "p_rpt_cif089_1.sql",
            "P_RPT_CIF089KN.sql",
            "P_RPT_CIF089KP.sql",
            "p_rpt_cif330d.sql",
            "p_rpt_fxd344rp.sql",
            "P_RPT_SAV_CUR_FLOAT.sql",
            "p_rpt_tu_error_mid.sql",
        ]
        self.setProcedurePath()

    def setProcedurePath(self):
        if platform.uname().system == "Windows":
            self.procedure_path = configs.get("path").get("win_svn_procedure_path")
        else:
            self.procedure_path = configs.get("path").get("svn_procedure_path")

    def getSvnStList(self):
        os.chdir(self.procedure_path)
        svn_st_list = os.popen("svn st").read().strip("\n").split("\n")
        return svn_st_list

    def findProcedureModifyList(self):
        svn_st_list = self.getSvnStList()
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
        return svn_list

    def isAllProcedureCorrect(self) -> bool:
        procedure_list = self.findProcedureModifyList()
        check_pass = True
        for procedure in procedure_list:
            if procedure not in self.white_list and not self.isOneProcedureCorrect(
                procedure
            ):
                check_pass = False
        return check_pass

    def isOneProcedureCorrect(self, procedure: str) -> bool:
        if self.isDateHardCode(procedure):
            print(
                "Warning: {} date is hard code, please check! __________________".format(
                    procedure
                )
            )
            return False
        return True

    def isDateHardCode(self, procedure: str) -> bool:
        """
        检查是否有将日期写死，如将v_deal_date 写date'20...'
        """
        with open(
            os.path.join(self.procedure_path, procedure), "r", encoding="utf-8"
        ) as f:
            proc_cont = f.read()
            if re.search("date'20", proc_cont, flags=re.IGNORECASE):
                return True

        return False


if __name__ == "__main__":
    a = CheckProcedure()
    # tests
    # assert a.isDateHardCode("p_rpt_lon800_2.sql") is False
    # a.isOneProcedureCorrect("p_rpt_lon800_2.sql")
    # a.findProcedureModifyList()
    a.isProcedureCorrects()
