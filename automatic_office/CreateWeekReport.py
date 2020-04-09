import datetime
import pysnooper
import pprint
import os
import sys
import shutil
import docx


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
        self.interval = DealInterval()

    @staticmethod
    def copy_file(from_end_str: str):
        from_dir = os.path.join("automatic_office", "doc_file")
        from_file = "创兴银行香港ODS项目周报_董坚_from_end_str.docx"
        shutil.copy(
            os.path.join(from_dir, from_file),
            os.path.join(from_dir, from_file.replace("from_end_str", from_end_str)),
        )

    @staticmethod
    def replace_date_str(content: str, date_name: str, date_str: str) -> str:
        if date_name in content:
            content = content.replace(date_name, date_str)
        return content

    @staticmethod
    def check_and_change(document, date_tuple: tuple):
        for para in document.paragraphs:
            for i, run in enumerate(para.runs):
                run.text = self.replace_date_str(
                    run.text, "from_end_str", self.interval.get_from_end_str(date_tuple)
                )
                run.text = self.replace_date_str(
                    run.text, "from_date", self.interval.get_from_date(date_tuple)
                )
                run.text = self.replace_date_str(
                    run.text, "end_date", self.interval.get_end_date(date_tuple)
                )
        return document

    def main(self):
        # todo
        weekdays = CheckInForm(self.year_month).get_all_work_date()
        for date_tuple in self.interval.get_all_weekday_interval(weekdays, []):
            from_end_str = self.interval.get_from_end_str(date_tuple)
            # from_date = self.interval.get_from_date(date_tuple)
            # end_date = self.interval.get_end_date(date_tuple)
            # copy file
            self.copy_file(from_end_str)
            # replace content


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        logging.info("Please input year_moth(YYYYMM)")
        sys.exit(1)

    obj = CreateWeekReport(sys.argv[1])
