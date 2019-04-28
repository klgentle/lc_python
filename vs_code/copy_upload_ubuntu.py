import shutil, os
import openpyxl
import pprint
import csv
from sys import argv


# copy upload register and upload file


class CopyRegister(object):
    def __init__(self):
        self.code_home = "/mnt/svn"
        self.dir_name = os.path.join(self.code_home, "1300_编码/发布登记表")
        code_bate_path = "/mnt/e/yx_walk/report_develop/sky"
        self.target_path = os.path.join(code_bate_path, date_str + "bate")
        os.makedirs(self.target_path, exist_ok=True)
        # self.date_str = date_str
        self.data_list = []

    def readRegister(self, date_str: str):
        """ copy register """

        for folderName, subfolders, filenames in os.walk(self.dir_name):
            for filename in filenames:
                # print('FILE INSIDE ' + folderName + ': '+ filename)
                if filename.find(date_str) > -1:
                    print(f"filename: {filename} --------------------------")
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
                        self.data_list.append(
                            sheet[chr(i + ord("A")) + str(row)].value
                            for i in range(0, 10)
                        )

    def saveRegister(self):

        csvFile = open(self.target_path + "/登记表" + date_str + ".csv", "w", newline="")
        csvWriter = csv.writer(csvFile, delimiter=",", lineterminator="\n")
        csvWriter.writerow(
            [
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
        )
        # print(f'self.date_list:{self.data_list}')
        # record rows
        for row in self.data_list:
            csvWriter.writerow(row)

        csvFile.close()

    def copyfiles(self):
        # copy code files
        for row in self.data_list:
            [name, file_type, path] = row[2:5]
            ind = path.find("1300_编码")
            if ind > -1:
                # new_path = os.path.join(self.code_home, path[ind:])
                new_file = os.path.join(
                    self.code_home, path[ind:], name + "." + file_type.lower()
                )
                # print(f"new_file:{new_file}")

                targetName = path[ind:].split("\\")[1].split("_")[1]
                # print(f"targetName:{targetName}")

                self.target_path2 = os.path.join(self.target_path, targetName)
                os.makedirs(self.target_path2, exist_ok=True)
                try:
                    shutil.copy(new_file, self.target_path2)
                except FileNotFoundError:
                    print(f"error! No such file: {new_file}")


if __name__ == "__main__":
    if len(argv) == 2 and len(argv[1]) == 8:
        a = CopyRegister()
        data_str = argv[1]
        #a.copyRegister(argv[1])
        readRegister(date_str)
        saveRegister()
        copyfiles()
    else:
        print("usage python[3] copy_upload_ubuntu.py '20190501'")
