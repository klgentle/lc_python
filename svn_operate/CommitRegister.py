import datetime
import platform
import time

from sys import argv
from date_add import date_add
from PlatformOperation import PlatformOperation
from SvnOperate import SvnOperate
from CheckProcedure import CheckProcedure
from ReleaseRegistrationForm import ReleaseRegistrationForm

SVN_DIR = "/mnt/e/svn/1300_编码/"
if platform.uname().system == "Windows":
    SVN_DIR = "E:\\svn\\1300_编码\\"


class CommitRegister(object):
    """ read log to write excel for install """

    def __init__(self, date_str, mantis, module_type):
        self.__mantis = mantis
        self.__registration = ReleaseRegistrationForm(date_str, mantis, module_type)

    @staticmethod
    def checkProcedureAndExit():
        # 检查存储过程
        cp = CheckProcedure()
        if not cp.isAllProcedureCorrect():
            sys.exit(1)

    def __getCommitMessage(self):
        commitMessage = ""
        if self.__mantis:
            commitMessage = f"mantis: {self.__mantis}"
        return commitMessage 

    def svn_add_commit(self):
        try:
            self.svn = SvnOperate(SVN_DIR)
            self.svn.svn_add()
            self.svn.svn_delete()
            self.svn.svn_commit_code(message=self.__getCommitMessage())
            self.svn.update_svn()
        except Exception as e:
            print("Svn Operate Error:", e.__doc__)

    def commit_register(self):
        try:
            self.svn.svn_add()
            self.svn.svn_commit()
        except Exception as e:
            print("svn error:", e.__doc__)
    
    def SvnLogRegist(self):
        self.__registration.logRead()
        self.__registration.logRegister()
    
    def SvnLogRegistAndCommit(self):
        self.checkProcedureAndExit()
        self.svn_add_commit()
        self.SvnLogRegist()
        self.commit_register()


if __name__ == "__main__":
    today = time.strftime("%Y%m%d", time.localtime())
    date_str = time.strftime("%Y%m%d", time.localtime())
    time_str = time.strftime("%H:%M", time.localtime())
    if time_str > "16:10":
        # today add one day
        date_str = date_add(1)
    mantis = ""
    module_type = "cif"

    if len(argv) == 2 and len(argv[1]) == 8:
        date_str = argv[1]
    elif len(argv) == 3:
        date_str, mantis = argv[1], argv[2]
    elif len(argv) == 4:
        date_str, mantis, module_type = argv[1], argv[2], argv[3]
        if not argv[3]:
            module_type = "cif"
    elif len(argv) > 4:
        print("usage: python3 commit_register.py '20190501' mantis_id, module_type")
        sys.exit(1)

    if len(argv) > 1 and argv[1].find("d+") > -1:
        # get days from d+days
        days = int(argv[1][2:])
        date_str = date_add(days)

    if date_str < today:
        print(f"date_str:{date_str} is wrong!")
        sys.exit(1)

    print(f"argv:{argv} ---------- ")
    print(f"date_str:{date_str} ---------- ")

    a = CommitRegister(date_str, mantis, module_type)
    a.SvnLogRegistAndCommit()
    print(f"time:{time_str}")
