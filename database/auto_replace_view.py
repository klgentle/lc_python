from ViewOperate import ViewOperate 
from Procedure import Procedure




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
        """检查是否存在要改的视图 """
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

        #procedure.data_area_deal()
        #print(f"{proc_name} data_area处理完成！")

    def replace_view_and_data_area(self, proc_name:str):
        self.view_replace(proc_name)
        procedure = Procedure(proc_name)
        procedure.data_area_deal()
        print(f"{proc_name} data_area处理完成！")


if __name__ == "__main__":
    obj = AutoViewReplace()
    #obj.replace_view_and_data_area("p_rpt_cif021")
    obj.replace_view_and_data_area("p_rpt_lgr001")

    # test data_area deal
    #procedure = Procedure("p_rpt_cif021")
    #procedure.data_area_deal()
    #print("data_area处理完成！")
