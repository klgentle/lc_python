import shutil, os
import openpyxl
import pprint
import codecs
import csv
import os
import time
import sh

from sys import argv
from openpyxl import Workbook
from backupToZip import backupToZip
from datetime import datetime

#from list_file import list_file


class CopyRegister(object):
    """ copy 'svn/1300_编码' upload register and upload file 
       "usage python[3] copy_upload_ubuntu.py '20190501'"
    """

    def __init__(self, date_str: str):
        self.date_str = date_str

        code_beta_path = "/mnt/e/yx_walk/report_develop/sky"
        self.code_home = "/mnt/e/svn"
        self.dir_name = os.path.join(self.code_home, "1300_编码/发布登记表")
        self.svnup_dir = os.path.join(self.code_home, "1300_编码")
        # BE CAREFUL HERE
        ###############os.system(f"svn up '{self.svnup_dir}'")

        self.target_path = os.path.join(code_beta_path, self.date_str + "beta")
        if os.path.exists(self.target_path):
            sh.rm("-rf", f"{self.target_path}")
        os.makedirs(self.target_path, exist_ok=True)

        self.data_list = []
        self.procedure_name_list = []
        # print(f"self.date_str:{self.date_str}")

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
                    data_row = [
                        sheet[chr(i + ord("A")) + str(row)].value for i in range(0, 10)
                    ]
                    if isinstance(data_row[7],datetime):
                        data_row[7] = data_row[7].strftime("%Y%m%d")

                    #print(f"data_row:{data_row}")
                    self.data_list.append(data_row)

        # print(f"data_list:{self.data_list}")

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
            elif file_type.upper() in ("PRO", "FNC"):
                file_type = "sql"
            # strip() delete blank
            name_and_type = name + '.' + file_type.lower().strip() 
            if name.find('.') > -1:
                name_and_type = name

            new_file = os.path.join(
                self.code_home, path[ind:], name_and_type
            )

            #print(f"path:{path}")
            # get folder name of code 
            targetName = path[ind:].split("/")[1]

            if targetName != "1350_存储过程":
                targetName = file_type
            self.target_path2 = os.path.join(self.target_path, targetName)
            os.makedirs(self.target_path2, exist_ok=True)
            try:
                shutil.copy(new_file, self.target_path2)
            except FileNotFoundError:
                print(f"error! No such file: {new_file} _______________")

    def saveRegisterExcel(self):
        # print(f"start to write rows! ")

        file1 = os.path.join(self.svnup_dir, "发布登记表", "支付", "ODS程序版本发布登记表(支付)-template.xlsx")
        file_path_name = self.target_path + "/登记表" + self.date_str + ".xlsx"
        # print(f"file_path_name:{file_path_name}")
        # print(f"file1:{file1}")
        shutil.copy(file1, file_path_name)

        # wb = Workbook()
        wb = openpyxl.load_workbook(file_path_name)
        sheet = wb.active
        # sheet.title = self.date_str + "发布登记"

        # record rows
        for row in self.data_list:
            sheet.append(row)

        wb.save(filename=file_path_name)

    #def createZipfile(self):
    #    return backupToZip(self.target_path)

    def list_file(self, path: str, file_name: str, path2: str):
        to_file = open(file_name, "w")
        #date_str = time.strftime("%Y%m%d", time.localtime())
        to_path = f"D:\jdong\\beta\\{self.date_str}beta\\{path2}"
        for f in os.listdir(path):
            s = f"@@{to_path}\{f};\n"
            to_file.write(s)
            if path2 == "1350_存储过程":
                # procedure name add to list
                pro_name = f.split(".")[0]
                self.procedure_name_list.append(pro_name.upper())

        to_file.write("commit;\n")
        to_file.close()

    def listSqlFile(self):
        path2 = "1350_存储过程"
        path = os.path.join(self.target_path,path2)
        file_name = os.path.join(self.target_path,'pro.sql')
        # list procedure
        if os.path.exists(path):
            self.list_file(path, file_name, path2)

        path2 = "SQL"
        path = os.path.join(self.target_path,path2)
        file_name = os.path.join(self.target_path,'list.sql')
        # list other sql 
        if os.path.exists(path):
            self.list_file(path, file_name, path2)
        
    def createConfigCheckSql(self):
        file_name = os.path.join(self.target_path,'config_check.sql')
        to_file = open(file_name, "w")
        #print(f"self.procedure_name_list:{self.procedure_name_list}")
        sql = f"""SELECT OBJECT_NAME FROM ALL_OBJECTS WHERE OWNER = 'RPTUSER' AND OBJECT_TYPE = 'PROCEDURE'
AND OBJECT_NAME IN ({", ".join(["'" + name + "'" for name in self.procedure_name_list])})
AND SUBSTR(OBJECT_NAME,-4) != '_MID'
MINUS
select OBJECT_NAME from ods_job_config where object_type = 'SP';
        """
        to_file.write(f"{sql}\n")
        to_file.close()


if __name__ == "__main__":
    date_str = time.strftime("%Y%m%d", time.localtime())
    if len(argv) > 1 and len(argv[1]) == 8:
        date_str = argv[1]

    a = CopyRegister(date_str)
    a.readRegister()
    a.saveRegisterExcel()
    a.copyfiles()
    a.listSqlFile()
    a.createConfigCheckSql()
    # not create zip file, need to add rpt files
    #a.createZipfile()
    print("Done!")

    # print("usage python[3] copy_upload_ubuntu.py '20190501'")
