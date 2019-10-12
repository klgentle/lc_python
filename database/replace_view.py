import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
# from database.FindViewOriginalTable import FindViewOriginalTable
# from database.Procedure import Procedure
from database.ProcedureLogModify import ProcedureLogModify
from database.AutoViewReplace import AutoViewReplace


def read_file_to_list(file_name: str) -> list:
    name_list = []
    with open(file_name, "r") as file:
        cont = file.read()
        name_list = cont.split("\n")
    return name_list


def batch_replace_view(proc_list: list):
    proc_list = ["p_rpt_" + x.lower() for x in proc_list]
    # proc_list = ["p_itf_" + x.lower() for x in proc_list]
    error_list = []
    for proc in proc_list:
        # modify view name, data_area
        try:
            proc_view = AutoViewReplace()
            proc_view.main(proc)
        except:
            error_list.append(proc)
            print(f"error, {proc}")

    return error_list


if __name__ == "__main__":
    # if len(sys.argv) <= 1:
    #    logging.info("Please input procedure_name")
    #    sys.exit(1)

    file_name = r"database\payment_list.txt"
    # file_name = r"database\deposit_report_list.txt"
    # file_name = r"database\bi_list.txt"
    proc_list = read_file_to_list(file_name)
    error_list = batch_replace_view(proc_list)
    print("-------------", error_list)
