import os
import openpyxl
import platform
import pprint
import shutil, os
import sys
import re

from PlatformOperation import PlatformOperation

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
            self.regi_dir, f"ODS程序版本发布登记表{self.__module_type}-{self.__date_str}.xlsx"
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
        return module

    def logReadOneLine(self, line):
        print(f"line:{line}")
        if line.find("application/octet-stream") > -1:
            line = line.replace("application/octet-stream", "").strip()

        path_file = line
        if line.find("1300_编码") > -1:
            path_file = line[line.find("1300_编码") :]
        else:
            path_file = line.split(" ")[-1]
            # add 1300
            path_file = os.path.join("1300_编码", path_file)
        path_file = PlatformOperation.change_path_sep(path_file)
        file_path = os.path.join("1000_编辑区", os.path.dirname(path_file))

        path_list = path_file.split(os.sep)
        file_list = path_list[-1].split(".")
        file_name = file_list[0]
        file_type = file_list[-1].replace("\n", "")
        # 兼容 windows
        file_path = file_path.replace(os.sep, "\\")
        module = self.__getModule(file_name)
        row = [module, "报表"] + [file_name, file_type, file_path] + self.__commit_list_end
        self.__comit_list.append(row)

    def logRead(self):
        with open(SVN_LOG, encoding=self.__getEncoding()) as svn_log:
            for line in svn_log.readlines():
                line = line.strip()
                if self.__isCodeLine(line) and not self.__isRegistrationLine(line):
                    self.logReadOneLine(line)

        self.printComitList(self.__comit_list)

    @staticmethod
    def printComitList(comit_list):
        print("records are as bellow:")
        for registrationRow in comit_list:
            print(registrationRow)

    def logRegister(self):
        wb = openpyxl.load_workbook(self.__registration_file)
        sheet = wb.active
        for i in self.__comit_list:
            sheet.append(i)

        wb.save(filename=self.__registration_file)
        print("excel write down!")


if __name__ == "__main__":
    pass
    #reg = ReleaseRegistrationForm()
