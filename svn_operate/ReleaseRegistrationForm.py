import os
import openpyxl
import platform
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
        self.__create_target_file()
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

    # @pysnooper.snoop()
    def logRead(self):
        if platform.uname().system == "Windows":
            svn_log = open(SVN_LOG, encoding="gb2312")
        else:
            svn_log = open(SVN_LOG, encoding="utf-8-sig")  # deal with \ufeff
        for line in svn_log.readlines():
            line = line.strip()
            print(f"line:{line}")
            if (
                line.startswith("Sending")
                or line.startswith("Adding")
                or line.startswith("Modified")
                or line.startswith("Modify")
            ):
                if line.find("ODS程序版本发布登记表") > -1:
                    continue
                # delete  application/octet-stream
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
                path = os.path.join("1000_编辑区", os.path.dirname(path_file))
                path_list = path_file.split(os.sep)
                # 跳过建表语句
                # if path_list[-2] == "1380_建表语句":
                #    continue

                file_list = path_list[-1].split(".")
                file_name = file_list[0]
                # modu = file_name.upper().split("RPT_")
                modu = re.split("RPT_|ITF_", file_name.upper())
                module = ""
                if len(modu) > 1:
                    module = modu[1][:3]

                file_type = file_list[-1].replace("\n", "")
                # 兼容 windows
                path = path.replace(os.sep, "\\")
                row = (
                    [module, "报表"] + [file_name, file_type, path] + self.__commit_list_end
                )
                self.__comit_list.append(row)

        svn_log.close()

    def logRegister(self):
        wb = openpyxl.load_workbook(self.__registration_file)
        sheet = wb.active

        # DELETE BLANK ROW
        if sheet.max_row > 200:
            num = 1
            for row in range(2, sheet.max_row + 1):
                file_name = sheet["C" + str(row)].value
                if file_name:
                    num += 1
                else:
                    # row is blank and row+1 is blank too
                    if not sheet["C" + str(row + 1)].value:
                        break
            sheet.delete_rows(row, sheet.max_row - num)

        print("records are as bellow:")
        for i in self.__comit_list:
            print(f"{i}")
            sheet.append(i)

        wb.save(filename=self.__registration_file)
        print("excel write down!")
