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
        self.from_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)) + "/../",
            "automatic_office",
            "doc_file",
        )
        self.from_file = "创兴银行香港ODS项目周报_董坚_fromEndStr.docx"

    def copy_file(self, target_file: str):
        # from_dir = "doc_file"
        shutil.copy(os.path.join(self.from_dir, self.from_file), target_file)

    @staticmethod
    def replace_date_str(content: str, date_name: str, date_str: str) -> str:
        if date_name in content:
            content = content.replace(date_name, date_str)
        return content

    def check_and_change(self, document, date_tuple: tuple):
        # TODO 怎么修改标题
        for para in document.paragraphs:
            for i, run in enumerate(para.runs):
                run.text = self.replace_date_str(
                    run.text, "fromEndStr", self.interval.get_from_end_str(date_tuple)
                )
                run.text = self.replace_date_str(
                    run.text, "from_date", self.interval.get_from_date(date_tuple)
                )
                run.text = self.replace_date_str(
                    run.text, "end_date", self.interval.get_end_date(date_tuple)
                )
                # test
                print(f"i:{i},run:{run.text}")
        return document

    def create_week_report(self):
        # todo
        weekdays = CheckInForm(self.year_month).get_all_work_date()
        for date_tuple in self.interval.get_all_weekday_interval(weekdays, []):
            from_end_str = self.interval.get_from_end_str(date_tuple)
            # from_date = self.interval.get_from_date(date_tuple)
            # end_date = self.interval.get_end_date(date_tuple)

            # 保存时要重命名,先建立临时文件
            temp_file_name = self.from_file.replace("fromEndStr", "".join(from_end_str,"_temp"))
            temp_file = os.path.join(self.from_dir, temp_file_name)
            # copy file
            self.copy_file(temp_file)
            # replace content
            document = docx.Document(temp_file)
            document = self.check_and_change(document, date_tuple)
            # 保存时文件对象会丢失
            # TODO 怎么用 python 修改 word 中的对象?
            document.save(temp_file.replace("_temp",""))
            print(f"delete temp file")
            shutil.rmtree(temp_file)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        logging.info("Please input year_moth(YYYYMM)")
        sys.exit(1)

    obj = CreateWeekReport(sys.argv[1])
