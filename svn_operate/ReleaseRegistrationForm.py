import os
import openpyxl
import platform
import pprint
import shutil, os
import sys
import re
import time


from sys import argv
from PlatformOperation import PlatformOperation
from skip_table_structure_change import skip_table_structure_change

SVN_DIR = "/mnt/e/svn/1300_编码/"
SVN_LOG = "/mnt/e/svn/commit.log"
if platform.uname().system == "Windows":
    SVN_DIR = "E:\\svn\\1300_编码\\"
    SVN_LOG = "E:\\svn\\commit.log"


class ReleaseRegistrationForm(object):
    def __init__(self, date_str, mantis, module_type):
        self.__date_str = date_str
        self.__module_type = module_type
        self.__createRegistrationFile()
        self.__comit_list = []
        self.__commit_list_end = ["Dongjian", "Gene", self.__date_str, mantis, "", ""]

    def __createRegistrationFile(self):
        self.regi_dir = os.path.join(SVN_DIR, "发布登记表", self.__module_type)
        template_file = os.path.join(
            self.regi_dir, f"ODS程序版本发布登记表({self.__module_type})-template.xlsx"
        )
        self.__registration_file = os.path.join(
            self.regi_dir, f"ODS程序版本发布登记表({self.__module_type})-{self.__date_str}.xlsx"
        )
        if not os.path.exists(self.__registration_file):
            shutil.copy(template_file, self.__registration_file)

    @staticmethod
    def __getEncoding():
        if platform.uname().system == "Windows":
            return "gb2312"
        else:
            # deal with \ufeff
            return "utf-8-sig"

    @staticmethod
    def __isCodeLine(line):
        if (
            line.startswith("Sending")
            or line.startswith("Adding")
            or line.startswith("Modified")
            or line.startswith("Modify")
        ):
            return True
        return False

    @staticmethod
    def __isFolderLine(line):
        # 如果为目录则返回true
        if line.startswith("Adding") and line.split('/')[-1].find(".") == -1:
            return True
        return False

    @staticmethod
    def __isRegistrationLine(line):
        if line.find("ODS程序版本发布登记表") > -1:
            return True
        return False

    @staticmethod
    def __getModule(file_name:str) -> str:
        modu = re.split("RPT_|ITF_", file_name.upper())
        module = ""
        if len(modu) > 1:
            module = modu[1][:3]
        return module or "CIF"

    @staticmethod
    def __svnLineClean(line):
        line = line.split(" ")[-1]
        line = line.replace("\n","")
        if line.find("application/octet-stream") > -1:
            line = line.replace("application/octet-stream", "").strip()
        return line

    def __getPathAndFileFrom(self, line):
        line = self.__svnLineClean(line)
        if line.find("1300_编码") > -1:
            pathAndFile = line[line.find("1300_编码") :]
        else:
            pathAndFile = os.path.join("1300_编码", line)
        pathAndFile = os.path.join("1000_编辑区", pathAndFile)
        pathAndFile = PlatformOperation.change_path_sep(pathAndFile)
        return pathAndFile

    def logReadOneLine(self, line):
        pathAndFile = self.__getPathAndFileFrom(line)
        filePath = os.path.dirname(pathAndFile)
        filenameAndType = os.path.basename(pathAndFile) 
        filename = filenameAndType.split(".")[0]
        filetype = filenameAndType.split(".")[-1]

        # 兼容 windows
        filePath = filePath.replace(os.sep, "\\")
        module = self.__getModule(filename)
        row = [module, "报表"] + [filename, filetype, filePath] + self.__commit_list_end
        self.__comit_list.append(row)

    def logRead(self):
        with open(SVN_LOG, encoding=self.__getEncoding()) as svn_log:
            for line in svn_log.readlines():
                line = line.strip()
                if self.__isCodeLine(line) and not self.__isRegistrationLine(line) and not self.__isFolderLine(line):
                    self.logReadOneLine(line)


    @staticmethod
    def printComitList(comit_list):
        print("records are as bellow:")
        for registrationRow in comit_list:
            print(registrationRow)

    def logRegister(self):
        wb = openpyxl.load_workbook(self.__registration_file)
        sheet = wb.active
        regist_list = skip_table_structure_change(self.__comit_list)
        self.printComitList(regist_list)
        for i in regist_list:
            sheet.append(i)

        wb.save(filename=self.__registration_file)
        print("excel write down!")


    def logClean(self):
        with open(SVN_LOG, "w") as svn_log:
            pass
        

if __name__ == "__main__":
    date_str = time.strftime("%Y%m%d", time.localtime())
    if argv[1]:
        date_str = argv[1]
    mantis = ""
    if len(argv) >2:
        mantis = argv[2]
    reg = ReleaseRegistrationForm(date_str, mantis, "cif")
    #reg.logRead()
    #reg.logRegister()
    reg.logClean()
