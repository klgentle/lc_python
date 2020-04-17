import datetime
import pysnooper
import pprint
import os
import sys
import shutil
import docx

import openpyxl


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
        self.from_excel = "创兴银行香港ODS项目周报_董坚_fromEndStr.xlsx"

    def copy_file(self, from_file, target_file: str):
        # from_dir = "doc_file"
        shutil.copy(os.path.join(self.from_dir, from_file), target_file)

    @staticmethod
    def replace_date_str(content: str, date_name: str, date_str: str) -> str:
        if date_name in content:
            content = content.replace(date_name, date_str)
        return content

    def replace_all_str(self, text: str, date_tuple: tuple) -> str:
        text = self.replace_date_str(
            text, "fromEndStr", self.interval.get_from_end_str(date_tuple)
        )
        text = self.replace_date_str(
            text, "fromDate", self.interval.get_from_date(date_tuple)
        )
        text = self.replace_date_str(
            text, "endDate", self.interval.get_end_date(date_tuple)
        )
        return text

    def check_word_change(self, document, date_tuple: tuple):
        for para in document.paragraphs:
            for i, run in enumerate(para.runs):
                run.text = self.replace_all_str(run.text, date_tuple)
                # test
                # print(f"i:{i},run:{run.text}")
        return document

    def check_excel_change(self, file_name, date_tuple: tuple):
        file_path = os.path.join(self.from_dir, file_name)
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active

        for row in range(1, sheet.max_row + 1):
            for col in range(1, sheet.max_column + 1):
                if sheet.cell(row, col).value in ("fromEndStr", "fromDate", "endDate"):
                    # print(f"excel value:[{sheet.cell(row, col).value}]")
                    # 替换单元格的值
                    sheet.cell(row, col).value = self.replace_all_str(
                        sheet.cell(row, col).value, date_tuple
                    )

        wb.save(file_path)

    def create_week_report(self):
        weekdays = CheckInForm(self.year_month).get_all_work_date()
        for date_tuple in self.interval.get_all_weekday_interval(weekdays, []):
            from_end_str = self.interval.get_from_end_str(date_tuple)

            word_file_name = self.from_file.replace("fromEndStr", from_end_str)
            word_file = os.path.join(self.from_dir, word_file_name)
            # copy word file
            self.copy_file(self.from_file, word_file)
            # replace content
            document = docx.Document(word_file)
            document = self.check_word_change(document, date_tuple)
            document.save(word_file)

            excel_file_name = self.from_excel.replace("fromEndStr", from_end_str)
            # copy excel file
            self.copy_file(self.from_excel, os.path.join(self.from_dir, excel_file_name))
            self.check_excel_change(excel_file_name, date_tuple)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        logging.info("Please input year_moth(YYYYMM)")
        sys.exit(1)

    obj = CreateWeekReport(sys.argv[1])
    obj.create_week_report()
