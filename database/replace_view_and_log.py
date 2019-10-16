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


def run_replace_view(proc_name: str):
    # modify view name, data_area
    proc_view = AutoViewReplace()
    proc_view.main(proc_name)


def run_modify_log(proc_name: str):
    # modify log
    proc_log = ProcedureLogModify(proc_name)
    proc_log.main()


if __name__ == "__main__":
    action = ""
    if len(sys.argv) <= 1:
        logging.info("Please input procedure_name")
        sys.exit(1)
    if len(sys.argv) >= 3:
        action = sys.argv[2]

    proc_name = sys.argv[1]
    if action.lower().startswith("v"):
        run_replace_view(proc_name)
    elif action.lower().startswith("l"):
        run_modify_log(proc_name)
    else:
        run_replace_view(proc_name)
        run_modify_log(proc_name)

