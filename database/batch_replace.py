import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
# from database.FindViewOriginalTable import FindViewOriginalTable
# from database.Procedure import Procedure
from database.ProcedureLogModify import ProcedureLogModify
from database.AutoViewReplace import AutoViewReplace


def run_replace_view(proc_name: str, schema="RPTUSER"):
    # modify view name, data_area
    proc_view = AutoViewReplace()
    proc_view.main(proc_name, schema)


def run_modify_log(proc_name: str, schema="RPTUSER"):
    # modify log
    # TODO add schema
    proc_log = ProcedureLogModify(proc_name)
    proc_log.main()


def read_file_to_list(file_name: str) -> list:
    name_list = []
    with open(file_name, "r") as file:
        cont = file.read()
        name_list = cont.split("\n")
    return name_list


def batch_replace(proc_list: list, replace_type="view_and_log"):
    error_dict = {}
    for content in proc_list:
        proc, schema = content.split("\t")
        if not schema:
            schema = "RPTUSER"
        # print(f"content:{content}")
        # print(f"proc:{proc}")
        # print(f"schema:{schema}")
        # modify view name, data_area
        try:
            # proc_view = AutoViewReplace()
            # proc_view.main(proc)
            if replace_type == "view":
                run_replace_view(proc, schema)
            elif replace_type == "log":
                run_modify_log(proc, schema)
            else:
                run_replace_view(proc, schema)
                run_modify_log(proc, schema)
        except Exception as e:
            # error_dict[proc] = e.__str__
            error_dict[proc] = e.__doc__
            print(f"error, {proc}, {schema}")

    return error_dict


if __name__ == "__main__":
    # if len(sys.argv) <= 1:
    #    logging.info("Please input procedure_name")
    #    sys.exit(1)

    file_name = r"E:\yx_walk\report_develop\view_to_replace\loan_list.txt"
    # proc_list = read_file_to_list(file_name)
    # proc_list = ["p_rpt_" + x.lower() for x in proc_list]
    # proc_list = ["p_itf_" + x.lower() for x in proc_list]
    proc_list = [
        "P_RPT_AFT019E	RPTUSER_MO",
        "P_RPT_CIF114D1	RPTUSER_MO",
        "P_RPT_CIF114D5	RPTUSER_MO",
        "P_RPT_ILN160	RPTUSER_MO",
        "P_RPT_ILN180B	RPTUSER_MO",
        "P_RPT_ILN200	RPTUSER_MO",
        "P_RPT_ILN200R	RPTUSER_MO",
        "P_RPT_ILN250	RPTUSER_MO",
        "P_RPT_ILN250A	RPTUSER_MO",
        "P_RPT_MACOA410	RPTUSER_MO",
        "P_RPT_MOR160	RPTUSER_MO",
    ]
    ###error_dict = batch_replace(proc_list, "view_and_log")
    # 尽量少改动
    error_dict = batch_replace(proc_list, "view")
    print("-------------", error_dict)
