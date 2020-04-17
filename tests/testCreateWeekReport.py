import os
import sys
from os.path import dirname
import datetime
import pprint
import unittest
import docx

# 项目根目录
BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
from automatic_office.CreateWeekReport import CreateWeekReport


class testCreateWeekReport(unittest.TestCase):
    def setUp(self):
        print("setUp...")
        self.report = CreateWeekReport("202003")
        self.from_file = self.report.from_file
        self.from_excel = self.report.from_excel
        self.target_file = os.path.join(
            self.report.from_dir,
            self.report.from_file.replace("fromEndStr", "20200305-20200306_temp"),
        )
        self.target_excel = os.path.join(
            self.report.from_dir,
            self.report.from_excel.replace("fromEndStr", "20200305-20200306"),
        )

    def test_copy_file(self):
        self.report.copy_file(self.from_file, self.target_file)
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)) + "/../",
            "automatic_office",
            "doc_file",
            "创兴银行香港ODS项目周报_董坚_20200305-20200306.docx",
        )
        assert os.path.exists(file_path) is True

    def test_replace_date_str(self):
        content = "lslldf from_end_str"
        assert (
            self.report.replace_date_str(content, "from_end_str", "20200305-20200306")
            == "lslldf 20200305-20200306"
        )

    def test_check_and_change(self):
        date_tuple = (datetime.date(2020, 3, 5), datetime.date(2020, 3, 6))
        # WHY 第一次测试时会报错，第二次却不会？路径有什么问题吗？
        document = docx.Document(self.target_file)
        document = self.report.check_word_change(document, date_tuple)
        document.save(self.target_file.replace("_temp", ""))
        # 无法 assert 只能肉眼看

    def test_copy_excel(self):
        self.report.copy_file(self.from_excel, self.target_excel)
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)) + "/../",
            "automatic_office",
            "doc_file",
            "创兴银行香港ODS项目周报_董坚_20200305-20200306.xlsx",
        )
        assert os.path.exists(file_path) is True

    def test_check_excel_change(self):
        file_name = "创兴银行香港ODS项目周报_董坚_20200305-20200306.xlsx"
        date_tuple = (datetime.date(2020, 3, 5), datetime.date(2020, 3, 6))
        self.report.check_excel_change(file_name, date_tuple)

    def tearDown(self):
        print("tearDown...")

        """
        ERROR: test_check_excel_change (__main__.testCreateWeekReport)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "testCreateWeekReport.py", line 69, in test_check_excel_change
    self.report.check_excel_change(file_name, date_tuple)
  File "/mnt/c/Users/pactera/lc_python/automatic_office/CreateWeekReport.py", line 77, in check_excel_change
    for row in range(sheet.get_rows()):
TypeError: 'generator' object cannot be interpreted as an integer
        """

if __name__ == "__main__":
    unittest.main()
