class AutoViewReplace(object):
    """视图改原表，自动化：
        1.自动查找视图，rptuser.v_, from v_, join v_
        2.data_area 处理：行首加--， behead where add 1=1 --
    """

    def __init__(self):
        pass

    def is_view_exits(self,procedure_name:str):
        """检查是否存在要改的视图"""
        pass

    def is_view_whitelist(self,vie_name:str)-> bool:
        """是否白名单（不需要修改）"""
        pass

    def view_replace(self):
        """替换视图"""
        pass

    def data_area_deal(self):
        """处理data_area"""
        pass


if __name__ == "__main__":
    obj = AutoViewReplace()
