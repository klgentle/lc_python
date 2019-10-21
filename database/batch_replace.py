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


def run_replace_view(proc_name: str):
    # modify view name, data_area
    proc_view = AutoViewReplace()
    proc_view.main(proc_name)


def run_modify_log(proc_name: str):
    # modify log
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
    for proc in proc_list:
        # modify view name, data_area
        try:
            # proc_view = AutoViewReplace()
            # proc_view.main(proc)
            if replace_type == "view":
                run_replace_view(proc)
            elif replace_type == "log":
                run_modify_log(proc)
            else:
                run_replace_view(proc)
                run_modify_log(proc)
        except Exception as e:
            # error_dict[proc] = e.__str__
            error_dict[proc] = e.__doc__
            print(f"error, {proc}")

    return error_dict


if __name__ == "__main__":
    # if len(sys.argv) <= 1:
    #    logging.info("Please input procedure_name")
    #    sys.exit(1)

    # file_name = r"database\payment_list.txt"
    # file_name = r"E:\yx_walk\report_develop\view_to_replace\deposit_report_list.txt"
    # file_name = r"E:\yx_walk\report_develop\view_to_replace\cif_list.txt"
    ## file_name = r"E:\yx_walk\report_develop\view_to_replace\bi_list.txt"
    # proc_list = read_file_to_list(file_name)
    # proc_list = ["p_rpt_" + x.lower() for x in proc_list]
    # proc_list = ["p_itf_" + x.lower() for x in proc_list]
    proc_list = [
        "p_rpt_cif058",
        "p_rpt_cif150",
        "p_rpt_cif613_3",
        "p_rpt_cifsb013",
        "p_rpt_cif088e",
        "p_rpt_cif088k",
        "p_rpt_cif088rc",
        "p_rpt_cif089_1",
        "p_rpt_cif089c1",
        "p_rpt_cif089c2",
        "p_rpt_cif089cn",
        "p_rpt_cif089cp",
        "p_rpt_cif089ka",
        "p_rpt_cif089kn",
        "p_rpt_cif089kp",
        "p_rpt_cif089r1",
        "p_rpt_cif089r2",
        "p_rpt_cif089rn",
        "p_rpt_cif089rp",
        "p_rpt_cif096",
    ]
    error_dict = batch_replace(proc_list, "view_and_log")
    print("-------------", error_dict)
