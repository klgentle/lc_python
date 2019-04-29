import shutil, os
import openpyxl
import pprint
import csv
from sys import argv
import codecs


class CopyRegister(object):
    """ copy upload register and upload file """
    def __init__(self,date_str:str):
        self.date_str = date_str 

        self.code_home = "/mnt/e/svn"
        self.dir_name = os.path.join(self.code_home, "1300_编码/发布登记表")
        code_bate_path = "/mnt/e/yx_walk/report_develop/sky"
        self.target_path = os.path.join(code_bate_path, self.date_str + "bate")
        os.makedirs(self.target_path, exist_ok=True)
        self.data_list = []
        print(f"self.date_str:{self.date_str}")

    def readRegister(self):
        """ copy register """

        for folderName, subfolders, filenames in os.walk(self.dir_name):
            for filename in filenames:
                #print('FILE INSIDE ' + folderName + ': '+ filename)
                if filename.find(self.date_str) == -1:
                    continue

                #print(f"filename: {filename} --------------------------")
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
                        sheet[chr(i + ord("A")) + str(row)].value
                        for i in range(0, 10)
                    ]
                    #print(f"data_row:{data_row}")
                    self.data_list.append(data_row)

        #print(f"data_list:{self.data_list}")

    def saveRegister(self):

        csvFile = open(self.target_path + "/登记表" + self.date_str + ".csv", "w", encoding='utf-8-sig')
        csvWriter = csv.writer(csvFile, delimiter=",", lineterminator="\n", dialect='excel')
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
                "remarks"
            ]
        #head_list = [str(i).encode('gbk','ignore') for i in head_list]
        csvWriter.writerow(head_list)
        # print(f'self.date_list:{self.data_list}')

        # record rows
        for row in self.data_list:
            csvWriter.writerow(row)

        csvFile.close()

    def copyfiles(self):
        # copy code files
        print(f"\n\nstart to write rows ----------------- ")
        for row in self.data_list:
            name, file_type, path = row[2:5]
            path = path.replace('\\','/')
            ind = path.find("1300_编码")
            if ind == -1:
                continue
            if file_type.upper() == 'BO':
                file_type = 'rpt'
            elif file_type.upper() == 'PRO':
                file_type = 'sql'

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


if __name__ == "__main__":
    if len(argv) == 2 and len(argv[1]) == 8:
        a = CopyRegister(argv[1])
        #a.date_str = argv[1]
        a.readRegister()
        a.saveRegister()
        a.copyfiles()
    else:
        print("usage python[3] copy_upload_ubuntu.py '20190501'")
