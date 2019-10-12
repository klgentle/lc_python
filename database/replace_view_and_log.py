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


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        logging.info("Please input procedure_name")
        sys.exit(1)

    proc_name = sys.argv[1]
    # modify view name, data_area
    proc_view = AutoViewReplace()
    proc_view.main(proc_name)
    # modify log
    # proc_log = ProcedureLogModify(proc_name)
    # proc_log.main()
