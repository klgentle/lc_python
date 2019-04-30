import shutil, os
import openpyxl
import pprint
import codecs
import csv
import os
import time
from sys import argv
from openpyxl import Workbook
from backupToZip import backupToZip

SVN_DIR = "/mnt/e/svn/1300_编码/"

class CopyRegister(object):
    """ copy 'svn/1300_编码' upload register and upload file 
       "usage python[3] copy_upload_ubuntu.py '20190501'"
    """

    def __init__(self, date_str: str):
        self.date_str = date_str

        self.code_home = "/mnt/e/svn"
        self.dir_name = os.path.join(self.code_home, "1300_编码/发布登记表")
        svnup_dir = os.path.join(self.code_home, "1300_编码")
        os.system(f"svn up '{svnup_dir}'")
        code_beta_path = "/mnt/e/yx_walk/report_develop/sky"
        self.target_path = os.path.join(code_beta_path, self.date_str + "beta")
        os.makedirs(self.target_path, exist_ok=True)
        self.data_list = []
        print(f"self.date_str:{self.date_str}")


    def readRegister(self):
        """ copy register """

        for folderName, subfolders, filenames in os.walk(self.dir_name):
            for filename in filenames:
                # print('FILE INSIDE ' + folderName + ': '+ filename)
                if filename.find(self.date_str) == -1:
                    continue

                # print(f"filename: {filename} --------------------------")
                whole_filename = os.path.join(folderName, filename)

                # copy excel file content
                wb = openpyxl.load_workbook(whole_filename)
                sheet = wb.active
                for row in range(2, sheet.max_row + 1):
                    name = sheet["C" + str(row)].value
                    if not name:
                        continue
                    # file_type = sheet["D" + str(row)].value
                    # path = sheet["E" + str(row)].value
                    data_row = [
                        sheet[chr(i + ord("A")) + str(row)].value for i in range(0, 10)
                    ]
                    # print(f"data_row:{data_row}")
                    self.data_list.append(data_row)

        # print(f"data_list:{self.data_list}")

    def saveRegister(self):

        csvFile = open(
            self.target_path + "/登记表" + self.date_str + ".csv",
            "w",
            encoding="utf-8-sig",
        )
        csvWriter = csv.writer(
            csvFile, delimiter=",", lineterminator="\n", dialect="excel"
        )
        head_list = [
            "所属模块",
            "类型（接口\报表）",
            "程序名称",
            "程序类型（pro\java\\rpt\sql\shell)",
            "SVN存储目录 ",
            "开发负责人",
            "BA负责人",
            "发布日期",
            "mantis id",
            "remarks",
        ]
        # head_list = [str(i).encode('gbk','ignore') for i in head_list]
        csvWriter.writerow(head_list)
        # print(f'self.date_list:{self.data_list}')

        # record rows
        for row in self.data_list:
            csvWriter.writerow(row)

        csvFile.close()

    def copyfiles(self):
        # copy code files
        for row in self.data_list:
            name, file_type, path = row[2:5]
            path = path.replace("\\", "/")
            ind = path.find("1300_编码")
            if ind == -1:
                continue
            if file_type.upper() == "BO":
                file_type = "rpt"
            elif file_type.upper() == "PRO":
                file_type = "sql"

            new_file = os.path.join(
                self.code_home, path[ind:], name + "." + file_type.lower()
            )
            # print(f"new_file:{new_file}")

            targetName = path[ind:].split("/")[1].split("_")[1]
            # print(f"targetName:{targetName}")

            self.target_path2 = os.path.join(self.target_path, targetName)
            os.makedirs(self.target_path2, exist_ok=True)
            try:
                shutil.copy(new_file, self.target_path2)
            except FileNotFoundError:
                print(f"error! No such file: {new_file}")

    def saveRegisterExcel(self):
        print(f"\n\nstart to write rows ----------------- ")

        file1 = os.path.join(SVN_DIR, "发布登记表", "支付", "ODS程序版本发布登记表(支付)-template.xlsx")
        file_path_name = self.target_path + "/登记表" + self.date_str + ".xlsx"
        print(f"file_path_name:{file_path_name}")
        if not os.path.exists(file_path_name):
            shutil.copy(file1, file_path_name)


        #wb = Workbook()
        wb = openpyxl.load_workbook(file_path_name)
        sheet = wb.active
        #sheet.title = self.date_str + "发布登记"

        #head_list = [
        #    "所属模块",
        #    "类型（接口\报表）",
        #    "程序名称",
        #    "程序类型（pro\java\\rpt\sql\shell)",
        #    "SVN存储目录 ",
        #    "开发负责人",
        #    "BA负责人",
        #    "发布日期",
        #    "mantis id",
        #    "remarks",
        #]
        #sheet.append(head_list)
        ## print(f'self.date_list:{self.data_list}')

        # record rows
        for row in self.data_list:
            sheet.append(row)

        wb.save(filename=file_path_name)

    def createZipfile(self):
        return backupToZip(self.target_path)


if __name__ == "__main__":
    date_str = time.strftime("%Y%m%d", time.localtime())
    if len(argv) > 1 and len(argv[1]) == 8:
        date_str = argv[1]

    a = CopyRegister(date_str)
    a.readRegister()
    a.saveRegisterExcel()
    a.copyfiles()
    a.createZipfile()

    # print("usage python[3] copy_upload_ubuntu.py '20190501'")
