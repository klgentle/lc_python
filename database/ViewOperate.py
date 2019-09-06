import os
import json
import sys


class ViewOperate(object):
    def __init__(self):
        self.view_path = "/home/kl/svn/1300_编码/1301_ODSDB/RPTUSER/03Views"
        self.new_path = "/mnt/e/yx_walk/report_develop/new_views"
        self.new_dict_file_name = "view_original_dict.txt"
        self.view_original_dict = {}

    def read_view_original_table(self, file_name: str):
        view_file = os.path.join(self.view_path, file_name)
        view_content = ""
        try:
            with open(view_file) as f:
                view_content = f.read().strip().upper()
            # return original table name, such as ODSUSER.CBS_FH00_TU_CUS_DETAILS_M
            # TODO deal with special data such as " from  ods"
            original_table = view_content.split("FROM ")[1].replace(";", "")
            return original_table.split("UNION")[0]
        except:
            return -1

    def read_all_view_original_table(self):
        for file_name in os.listdir(self.view_path):
            if not file_name.lower().startswith("v_"):
                continue
            # delete .sql for view_name
            view_name = file_name[:-4].upper()
            self.view_original_dict[view_name] = self.read_view_original_table(
                file_name
            )

        return self.view_original_dict

    def save_original_table_dict(self):
        # wirte file
        new_view = os.path.join(self.new_path, self.new_dict_file_name)
        with open(new_view, "w", encoding="utf-8") as new_f:
            new_f.write(json.dumps(self.read_all_view_original_table()))

    def get_view_original_table(self, view_name: str):
        if view_name.upper().startswith("RPTUSER"):
            view_name = view_name[8:]
        view_dict_file = os.path.join(self.new_path, self.new_dict_file_name)
        with open(view_dict_file) as f:
            view_dict = json.loads(f.read())
        return view_dict.get(view_name.upper())

    def create_view_to_table_sql(self):
        view_dict_file = os.path.join(self.new_path, self.new_dict_file_name)
        with open(view_dict_file) as f:
            view_dict = json.loads(f.read())

        sql_list = []
        view_sql = os.path.join(self.new_path, "view_sql.sql")
        with open(view_sql, "w", encoding="utf-8") as new_f:
            for view_name, table_name in view_dict.items():
                # V_ACCOUNT_ALL
                view_short_name = view_name[2:-4]
                sql = f"insert into view_to_table (view_name, table_name, view_short_name) values('{view_name}','{table_name.strip()}','{view_short_name}'); "
                # sql_list.append(sql)
                new_f.write(sql + "\n")


if __name__ == "__main__":
    # use for search table
    if len(sys.argv) <= 1:
        print("Please input view_name")
        sys.exit(1)

    a = ViewOperate()
    # original_table = a.read_view_original_table('v_limit_all.sql')
    # print(original_table)
    # a.create_view_to_table_sql()
    # use for search table
    print(a.get_view_original_table(sys.argv[1]))
