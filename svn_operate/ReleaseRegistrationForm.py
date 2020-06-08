import os
import platform

class ReleaseRegistrationForm(object):

    def __init__(self, date_str, mantis, module_type):
        self.checkProcedureAndExit()
        
        # 提交SVN
        try:
            self.svn_add_commit()
        except Exception as e:
            print("Svn Operate Error:", e.__doc__)

        self.create_target_file()
        self.comit_list = []
        self.commit_list_end = ["Dongjian", "Gene", self.date_str, mantis, "", ""]

    def create_target_file(self):
        # copy template change excel name
        self.regi_dir = os.path.join(SVN_DIR, "发布登记表", module_type)

        target_file = os.path.join(
            self.regi_dir, f"ODS程序版本发布登记表({module_type})-template.xlsx"
        )
        self.date_str = date_str
        module_type_name = f"({module_type})"
        if module_type.upper() == "DEPOSIT":
            module_type_name = ""
        self.__source_file = os.path.join(
            self.regi_dir, f"ODS程序版本发布登记表{module_type_name}-{self.date_str}.xlsx"
        )
        # print(f"self.__source_file:{self.__source_file}")
        if not os.path.exists(self.__source_file):
            shutil.copy(target_file, self.__source_file)

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
                path_file = ReleaseRegistrationForm.change_path_sep(path_file)
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
                    [module, "报表"] + [file_name, file_type, path] + self.commit_list_end
                )
                self.comit_list.append(row)

        svn_log.close()
    
    def logRegister(self):
        wb = openpyxl.load_workbook(self.__source_file)
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
        for i in self.comit_list:
            print(f"{i}")
            sheet.append(i)

        wb.save(filename=self.__source_file)
        print("excel write down!")

