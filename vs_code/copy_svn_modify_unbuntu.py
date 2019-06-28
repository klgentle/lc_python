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
from send_mail_with_attach import mail

#from list_file import list_file


class CopyRegister(object):
    """ copy 'svn/1300_编码' upload register and upload file 
       "usage python[3] copy_upload_ubuntu.py '20190501'"
    """

    def __init__(self, date_str: str):
        self.date_str = date_str

        home_path = "/home/kl"
        if not os.path.exists(home_path):
            home_path = "/mnt/e"

        self.code_beta_path = os.path.join(home_path, "yx_walk/beta")
        self.code_home = os.path.join(home_path, "svn")
        self.dir_name = os.path.join(self.code_home, "1300_编码/发布登记表")
        self.svnup_dir = os.path.join(self.code_home, "1300_编码")

        with os.popen("uname -a") as p :
            uname = p.read()
            if uname.find("Microsoft") == -1:
                # BE CAREFUL HERE ############### 
                # linux test
                os.system(f"svn up '{self.svnup_dir}'")

        self.target_path = os.path.join(self.code_beta_path, self.date_str + "beta")
        if os.path.exists(self.target_path):
            print(f"rm -rf {self.target_path}")
            sh.rm("-rf", f"{self.target_path}")
        os.makedirs(self.target_path, exist_ok=True)

        self.data_list = []
        self.procedure_name_list = []
	
        self.bo_name_list = []
        # print(f"self.date_str:{self.date_str}")

    def readRegister(self):
        """ copy register """

        for folderName, subfolders, filenames in os.walk(self.dir_name):
            for filename in filenames:
                # print('FILE INSIDE ' + folderName + ': '+ filename)
                # find right date register excel
                if filename.find(self.date_str) == -1:
                    continue

                # print(f"filename: {filename} --------------------------")
                whole_filename = os.path.join(folderName, filename)

                # copy excel file content
                wb = openpyxl.load_workbook(whole_filename)
                sheet = wb.active
                for row in range(2, sheet.max_row + 1):
                    name = sheet["C" + str(row)].value
                    # skip no name row record 
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
        error_file_type = set()
        # copy code files
        for row in self.data_list:
            name, file_type, path = row[2:5]
            path = path.replace("\\", "/")
            ind = path.find("1300_编码")

            if ind == -1:
                error_file_type.add('lost')
                print(f"path error, skip row: {name}, {file_type}, {path}")
                continue
            if file_type.upper() == "BO":
                file_type = "rpt"
            elif file_type.upper() in ("PRO", "FNC"):
                file_type = "sql"
            # fixing file_type
            elif file_type.upper() != "RPT" and path.find("1370_水晶报表") > -1: 
                file_type = "rpt"

            if file_type.upper() in ("RPT","BO"):
                self.bo_name_list.append(name)
                # name format: rpt to upper
                name = name.upper()

            # strip() delete blank
            name_and_type = name + '.' + file_type.lower().strip() 
            name_lower_type = name.lower() + '.' + file_type.lower().strip() 

            if name.find('.') > -1: # too smart
                name_and_type = name

            new_file = os.path.join(
                self.code_home, path[ind:], name_and_type
            )
            new_file2 = os.path.join(
                self.code_home, path[ind:], name_lower_type
            )

            #print(f"new_file:{new_file}")
            # get folder name of code 
            # get the file type name to depart pro and sql
            targetName = path[ind:].split("/")[-1]

            if targetName in ("1350_存储过程","05Procedures"):
                targetName = "pro" 
                self.procedure_name_list.append(name.upper())
            else:
                targetName = file_type.lower()

            self.target_path2 = os.path.join(self.target_path, targetName)
            os.makedirs(self.target_path2, exist_ok=True)
            try:
                # todo copy ignore upper or lower
                shutil.copy(new_file, self.target_path2)
            except FileNotFoundError:
                if os.path.exists(new_file2):
                    shutil.copy(new_file2, self.target_path2)
                else:
                    error_file_type.add(file_type.lower())
                    print(f"error! No such file: {new_file} _______________")

        return error_file_type

    def saveRegisterExcel(self):
        "save excel records to one excel"
        file1 = os.path.join(self.svnup_dir, "发布登记表", "支付", "ODS程序版本发布登记表(支付)-template.xlsx")
        file_path_name = self.target_path + "/登记表" + self.date_str + ".xlsx"
        shutil.copy(file1, file_path_name)

        # wb = Workbook()
        wb = openpyxl.load_workbook(file_path_name)
        sheet = wb.active
        # sheet.title = self.date_str + "发布登记"

        # record rows
        for row in self.data_list:
            sheet.append(row)

        wb.save(filename=file_path_name)

    def createZipfile(self):
        return backupToZip(self.target_path)

    def list_file(self, path: str, file_name: str, path2: str):
        to_file = open(file_name, "w")
        to_path = f"D:\jdong\\beta\\{self.date_str}beta\\{path2}"
        for f in os.listdir(path):
            s = f"@@{to_path}\{f};\n"
            to_file.write(s)

        to_file.write("commit;\n")
        to_file.close()

    def list_file2(self, path: str, file_name: str, path2: str):
        to_file = open(file_name, "w")

        to_file.write(f"set define off\nspool {self.date_str}_{path2}.log\n\n")
        for file_name in os.listdir(path):
            # 跳过目标文件
            if file_name in ("pro.sql","list.sql"):
                continue
            name_without_type = file_name.split(".")[0]
            s = f"prompt\n@@{file_name}\nprompt\nprompt {name_without_type}\nprompt ==============================\nprompt\n"
            to_file.write(s)

        to_file.write("\nspool off\ncommit;\n")
        to_file.close()

    def listSqlFile(self):
        dc = {
            "pro":"pro.sql",
            "sql":"list.sql"
        }
        for k, v in dc.items():
            path2 = k 
            path = os.path.join(self.target_path,path2)
            #file_name = os.path.join(self.target_path, v)
            file_name = os.path.join(path, v)
            # list file 
            if os.path.exists(path):
                self.list_file2(path, file_name, path2)
        
    def createConfigCheckSql(self):
        file_name = os.path.join(self.target_path,'config_check.sql')
        to_file = open(file_name, "w")
        # print test
        #print(f"self.procedure_name_list:{self.procedure_name_list}")
        sql = f"""SELECT OBJECT_NAME FROM ALL_OBJECTS WHERE OWNER = 'RPTUSER' AND OBJECT_TYPE = 'PROCEDURE'
AND OBJECT_NAME IN ({", ".join(["'" + name + "'" for name in self.procedure_name_list])})
AND SUBSTR(OBJECT_NAME,-4) != '_MID'
MINUS
select OBJECT_NAME from ods_job_config where object_type = 'SP';
        """
        to_file.write(f"{sql}\n")
        to_file.close()

    def boNameList(self,file_name='bo_list.txt'):
        self.bo_name_list.sort()
        print("\n请核对今日BO上线清单：\n"+'\n'.join(self.bo_name_list)+"\n")

        file_name = os.path.join(self.target_path,file_name)
        to_file = open(file_name, "w")
        to_file.write("请核对今日BO上线清单：\n")
        for b in self.bo_name_list:
            to_file.write(b+'\n')

        to_file.close()

    def send_mail(self,file_path=""):
        if not file_path:
            file_path = os.path.join(self.code_beta_path, self.date_str + "beta.zip")
        mail(self.date_str,file_path)

if __name__ == "__main__":
    date_str = time.strftime("%Y%m%d", time.localtime())
    if len(argv) > 1 and len(argv[1]) == 8:
        date_str = argv[1]

    a = CopyRegister(date_str)
    a.readRegister()
    a.saveRegisterExcel()
    error_file_type = a.copyfiles()
    a.listSqlFile()
    a.createConfigCheckSql()
    a.boNameList()
    # not create zip file, need to add rpt files
    a.createZipfile()
    # if only rpt not find, send email
    if not error_file_type or error_file_type == {'rpt'}:
        pass#a.send_mail()
    print("Done!")

    # print("usage python[3] copy_upload_ubuntu.py '20190501'")
