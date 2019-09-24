import os
from ViewOperate import ViewOperate

class Procedure(object):
    """
    procedure deal with path, procedure file name
    TODO 本程序有一个缺陷，会全部大写，如果需要小写的，要特别注意
    """
    def __init__(self, proc_name:str):
        self.__procedure_path = r"E:\svn\1300_编码\1301_ODSDB\RPTUSER\05Procedures"
        self.__proc_name = proc_name
        self.check_and_write_schema()

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
    
    @staticmethod
    def string_replace(src_cont:str, from_str:str, to_str:str)-> str:
        src_cont = src_cont.replace(from_str, to_str)
        return src_cont

    def replace_view_with_table(self, view_dict:dict):
        proc_cont = self.read_proc_cont()
        for view, table in view_dict.items(): 
            proc_cont = self.string_replace(proc_cont, view, table)
        self.write_procedure(proc_cont)

    def data_area_deal(self):
        """处理data_area
            TODO
            按行读取，如果出现了 on data_area, and data_area, where data_area,则在行首添加--
        """
        pass


class AutoViewReplace(object):
    """视图改原表，自动化：
        1.自动查找视图，rptuser.v_, from v_, join v_
        2.data_area 处理：行首加--， behead where add 1=1 --
    """
    def __init__(self):
        pass

    def procedure_view_set(self,proc_name:str) -> set:
        """返回视图集合"""
        view_set = set()

        procedure = Procedure(proc_name)
        proc_cont = procedure.read_proc_cont()
        #print(f"proc_cont:{proc_cont}")
        # find view name
        while self.view_index(proc_cont) > -1:
            view_ind = self.view_index(proc_cont)
            proc_from_index = proc_cont[view_ind:]
            view_name, *proc_cont_list = proc_from_index.split(' ')
            if not self.is_whitelist(view_name):
                view_set.add(view_name)
            # deal with proc_cont_list
            proc_cont = ' '.join(proc_cont_list)
        return view_set

    def view_index(self, proc_cont:str) -> int:
        """检查是否存在要改的视图
        """
        index = proc_cont.find('RPTUSER.V_') 
        return index 

    def is_whitelist(self,view_name:str)-> bool:
        """是否白名单（不需要修改）的视图"""
        return False
    
    def view_replace(self,proc_name:str):
        """替换视图"""
        proc_view_set = self.procedure_view_set(proc_name)
        if not proc_view_set:
            return

        # get view table
        proc_view_dict = {}
        view_obj = ViewOperate()
        for view in proc_view_set:
            table_name = view_obj.get_view_original_table(view) 
            proc_view_dict[view] = table_name

        procedure = Procedure(proc_name)
        procedure.replace_view_with_table(proc_view_dict)
        print(f"{proc_name} 视图已经改为原表！")
        procedure.data_area_deal()
        print(f"{proc_name} data_area处理完成！")



if __name__ == "__main__":
    obj = AutoViewReplace()
    #view_set = obj.procedure_view_set("p_rpt_cif035")
    #view_set = obj.procedure_view_set("p_rpt_cif025")
    view_set = obj.procedure_view_set("p_rpt_cif021")
    print(view_set)
    obj.view_replace("p_rpt_cif021")

    #pro = Procedure('p_rpt_cif021')

    
