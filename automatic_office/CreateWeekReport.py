import datetime
import pysnooper
import pprint
import os
import sys
import shutil


# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from automatic_office.CheckInForm import CheckInForm
from automatic_office.DealInterval import DealInterval

"""
根据工作日期，生成周报模板
"""


class CreateWeekReport(object):
    def __init__(self, year_month: str):
        if len(year_month) != 6:
            print("Please input year_month with format: YYYYMM!")
            sys.exit(1)
        self.year_month = year_month

    def copy_file(self):
        # todo
        weekdays = CheckInForm(self.year_month).get_all_work_date()
        interval = DealInterval()
        for date_tuple in interval.get_all_weekday_interval(weekdays, []):
            from_end_str = interval.get_from_end_str()
            from_date = interval.get_from_date()
            end_date = interval.get_end_date()
            # copy file
            from_dir = os.path.join("automatic_office", "doc_file")
            from_file = "创兴银行香港ODS项目周报_董坚_from_end_str.docx"
            shutil.copy(
                os.path.join(from_dir, from_file),
                os.path.join(from_dir, from_file.replace("from_end_str", from_end_str)),
            )


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        logging.info("Please input year_moth(YYYYMM)")
        sys.exit(1)

    obj = CreateWeekReport(sys.argv[1])
