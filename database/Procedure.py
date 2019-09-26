import os
from convert_file_to_utf8 import convert_file_to_utf8


class Procedure(object): 
    """ procedure deal with path, procedure file name 
    TODO 本程序有一个缺陷，会全部大写，如果需要小写的，要特别注意 """ 
    def __init__(self, proc_name:str): 
        self.__procedure_path = r"E:\svn\1300_编码\1301_ODSDB\RPTUSER\05Procedures" 
        self.__proc_name = proc_name 
        self.file_to_utf8()
        self.check_and_write_schema()
    
    def file_to_utf8(self):
        return convert_file_to_utf8(os.path.join(self.__procedure_path, self.get_file_name()))
                    
    def get_file_name(self) -> str:
        return self.__proc_name + '.sql'

    @staticmethod
    def need_add_schema(proc_cont:str) -> bool:
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
    
    def write_procedure(self, proc_cont:str):
        proc_file_name = self.get_file_name()
        with open(os.path.join(self.__procedure_path, proc_file_name),'w', encoding='UTF-8') as pro:
            pro.write(proc_cont)

    def read_proc_cont(self) -> str:
        proc_cont = ""
        proc_file_name = self.get_file_name()
        with open(os.path.join(self.__procedure_path, proc_file_name),'r', encoding='UTF-8') as pro:
            proc_cont = pro.read().upper()
        return proc_cont
    
    def replace_view_with_table(self, view_dict:dict):
        print("开始修改视图")
        proc_cont = self.read_proc_cont()
        for view, table in view_dict.items(): 
            proc_cont = proc_cont.replace(view, table)
        self.write_procedure(proc_cont)

    @staticmethod
    def data_area_check(line:str)-> bool:
        if line.find('DATA_AREA') > -1 and (line.find('ON ') > -1 or line.find('WHERE') > -1 or line.find('AND ') > -1):
            return True
        return False

    @staticmethod
    def data_area_replace(line:str)-> str:
        """ TODO
            按行读取，如果出现了 ON DATA_AREA, AND DATA_AREA, WHERE DATA_AREA,则进行替换，添加--
            ON, WHERE ->  ON 1=1 -- OR WHERE 1=1 -- 
            AND -> -- AND 
            ) -> \n)
        """
        print("修改data_area")
        if line.find('ON ') > -1:
            line = line.replace('ON ', 'ON 1=1 -- ')
        elif line.find('WHERE') > -1:
            line = line.replace('WHERE ', 'WHERE 1=1 -- ')
        elif line.find('AND ') > -1:
            line = line.replace('AND ', '--AND ')
        elif line.find(')') > -1:
            line = line.replace(')', '\n)')
        return line

    def data_area_deal(self):
        """处理data_area """
        proc_cont_list = []
        proc_file_name = self.get_file_name()
        with open(os.path.join(self.__procedure_path, proc_file_name),'r', encoding='UTF-8') as pro:
            proc_cont_list = pro.readlines()
        proc_cont_list = [item.upper() for item in proc_cont_list]
        for index, line in enumerate(proc_cont_list):
            if self.data_area_check(line):
                proc_cont_list[index] = self.data_area_replace(line)
                print("data_area处理")
                
        self.write_procedure("".join(proc_cont_list))
