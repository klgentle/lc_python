import openpyxl
import shutil, os
import time
from pprint import pprint
from sys import argv

SVN_DIR = "/mnt/e/svn/1300_编码/"
SVN_LOG = "/mnt/e/svn/commit.log"


class Solution:
    """
    """

    def __init__(self, date_str, remark):
        # svn up
        os.system(f"svn up '{SVN_DIR}'")
        # copy template change excel name
        self.regi_dir = os.path.join(SVN_DIR, "发布登记表", "支付")

        file1 = os.path.join(self.regi_dir, "ODS程序版本发布登记表(支付)-template.xlsx")
        self.date_str = date_str  # str time.strftime("%Y%m%d", time.localtime())
        self.file2 = os.path.join(
            self.regi_dir, f"ODS程序版本发布登记表(支付)-{self.date_str}.xlsx"
        )
        if not os.path.exists(self.file2):
            shutil.copy(file1, self.file2)
            # svn add
            # os.system(f"svn add '{self.file2}'")

        self.comit_list = []
        self.commit_list_head = ["支付", "报表"]
        self.commit_list_end = ["DONGJIAN", "DEVIL", self.date_str, "", remark]

    def logRead(self):
        svn_log = open(SVN_LOG)
        for line in svn_log.readlines():
            if line.startswith("Sending") or line.startswith("Adding"):
                if line.find("(bin)") > -1:
                    continue

                path_file = line.split("        ")[1]
                path_list = path_file.split("/")
                # 跳过建表语句
                if path_list[-2] == "1380_建表语句":
                    continue

                # print(f"path_list:{path_list}")
                path = "1000_编辑区\\" + "\\".join(path_list[:-1])
                file_list = path_list[-1].split(".")
                # print(f"file_list:{file_list}")
                file_name = file_list[0]
                file_type = file_list[-1].replace("\n", "")
                row = (
                    self.commit_list_head
                    + [file_name, file_type, path]
                    + self.commit_list_end
                )
                # print(f"row:{row}")
                self.comit_list.append(row)

        svn_log.close()
        # pprint(self.comit_list)

    def logRegister(self):
        wb = openpyxl.load_workbook(self.file2)
        sheet = wb.active
        for i in self.comit_list:
            sheet.append(i)

        wb.save(filename=self.file2)
        print("excel write down!")


if __name__ == "__main__":
    date_str = time.strftime("%Y%m%d", time.localtime())
    remark = ""
    #print(f"argv:{argv} ---------- ")
    if len(argv) == 2 and len(argv[1]) == 8:
        date_str = argv[1]
    elif len(argv) == 3:
        remark = argv[2]
    elif len(argv) > 3:
        print("usage: python3 commit_register.py '20190501' remark")
        sys.exit(1)

    a = Solution(date_str, remark)
    a.logRead()
    a.logRegister()
