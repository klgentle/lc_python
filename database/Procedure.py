import time
import sys
import os

# 项目根目录
from database.convert_file_to_utf8 import convert_file_to_utf8
from string_code.StringFunctions import StringFunctions
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
# 导入模块


class Procedure(object):
    """ procedure deal with path, procedure file name 
    TODO 本程序有一个缺陷，会全部大写，如果需要小写的，要特别注意 """

    def __init__(self, proc_name: str):
        self.__procedure_path = r"E:\svn\1300_编码\1301_ODSDB\RPTUSER\05Procedures"
        self.__proc_name = proc_name
        self.file_to_utf8()
        self.check_and_write_schema()
        self.__date_str = time.strftime("%Y%m%d", time.localtime())
        self.__note = "-- DONGJIAN {} ".format(self.__date_str)
        self.modify_proc_by_line()

    def file_to_utf8(self):
        return convert_file_to_utf8(os.path.join(self.__procedure_path, self.get_file_name()))

    def get_file_name(self) -> str:
        return self.__proc_name + '.sql'

    @staticmethod
    def need_add_schema(proc_cont: str) -> bool:
        """ check is exists FROM V_, JOIN V_
        """
        if (proc_cont.find("FROM V_") > -1 or proc_cont.find("JOIN V_") > -1
                or proc_cont.find("FROM RPT_") > -1 or proc_cont.find("JOIN RPT_") > -1):
            return True
        return False

    def check_and_write_schema(self):
        """ CHANGE FROM V_, JOIN V_ TO FROM RPTUSER.V_, JOIN RPTUSER.V_ """
        proc_cont = self.read_proc_cont()
        if self.need_add_schema(proc_cont):
            print("开始修改SCHEMA")
            # deal view
            proc_cont = proc_cont.replace("FROM V_", "FROM RPTUSER.V_")
            proc_cont = proc_cont.replace("JOIN V_", "JOIN RPTUSER.V_")
            # deal table
            proc_cont = proc_cont.replace("FROM RPT_", "FROM RPTUSER.RPT_")
            proc_cont = proc_cont.replace("JOIN RPT_", "JOIN RPTUSER.RPT_")
            self.write_procedure(proc_cont)

    @staticmethod
    def split_line_with_two_and(line: str):
        """TODO: more than one AND to add \n
            ON B1.ID = B3.ID AND B1.DATA_AREA = B3.DATA_AREA AND B1.DATA_DATE = B3.DATA_DATE
            line = self.split_two_and_line(line)
        """
        line_obj = StringFunctions(line)
        second_position = line_obj.find_the_second_position('AND ')
        line_strip = line.strip()
        if not line_strip.startswith('--') and not line_strip.startswith('WHEN') and second_position > -1:
            print('split line with two add')
            line = line_obj.str_insert(second_position, '\n')
        return line

    @staticmethod
    def deal_with_blanks(proc_cont:str)->str:
        """
        INSERT INTO  BAT_REPORT_LOG
        TODO use 正则表达式
        """
        return proc_cont

    def modify_proc_by_line(self):
        proc_cont_list = []
        proc_file_name = self.get_file_name()
        with open(os.path.join(self.__procedure_path, proc_file_name), 'r', encoding='UTF-8') as pro:
            proc_cont_list = pro.readlines()
        for i in range(0, len(proc_cont_list)):
            proc_cont_list[i] = self.split_line_with_two_and(proc_cont_list[i])

        self.write_procedure("".join(proc_cont_list))

    def write_procedure(self, proc_cont: str):
        proc_file_name = self.get_file_name()
        with open(os.path.join(self.__procedure_path, proc_file_name), 'w', encoding='UTF-8') as pro:
            pro.write(proc_cont)

    def read_proc_cont(self) -> str:
        proc_cont = ""
        proc_file_name = self.get_file_name()
        with open(os.path.join(self.__procedure_path, proc_file_name), 'r', encoding='UTF-8') as pro:
            proc_cont = pro.read().upper()
        return proc_cont

    def replace_view_with_table(self, view_dict: dict):
        print("开始修改视图")
        proc_cont = self.read_proc_cont()
        for view, table in view_dict.items():
            proc_cont = proc_cont.replace(view, table)
        self.write_procedure(proc_cont)

    @staticmethod
    def data_area_check(line: str) -> bool:
        if not line.strip().startswith('--') and line.find('DATA_AREA') > -1 and (line.find('ON ') > -1 or line.find('WHERE') > -1 or line.find('AND ') > -1):
            return True
        return False

    def data_area_replace(self, line: str) -> str:
        """ 
            按行读取，如果出现了 ON DATA_AREA, AND DATA_AREA, WHERE DATA_AREA,则进行替换，添加--
            ON, WHERE ->  ON 1=1 -- OR WHERE 1=1 -- 
            AND -> -- AND 
            ) -> \n)
        """
        if self.data_area_check(line):
            print("data_area处理")
            # if ON and AND in the same line, deal ADD only
            if line.find('AND ') > -1:
                line = line.replace('AND ', '--AND ')
            elif line.find('ON ') > -1:
                line = line.replace('ON ', 'ON 1=1 -- ')
            elif line.find('WHERE') > -1:
                line = line.replace(
                    'WHERE ', 'WHERE 1=1 -- ')
            elif line.find(')') > -1:
                line = line.replace(')', '\n)')
            # line add note in the end
            line = line[:-2] + self.__note + '\n'

        return line

    def data_area_deal(self):
        """处理data_area """
        proc_cont_list = []
        proc_file_name = self.get_file_name()
        with open(os.path.join(self.__procedure_path, proc_file_name), 'r', encoding='UTF-8') as pro:
            proc_cont_list = pro.readlines()
        proc_cont_list = [item.upper() for item in proc_cont_list]
        for index, line in enumerate(proc_cont_list):
            proc_cont_list[index] = self.data_area_replace(line)

        self.write_procedure("".join(proc_cont_list))


if __name__ == '__main__':
    proc = Procedure('p_rpt_cif022')
    proc.modify_proc_by_line()
