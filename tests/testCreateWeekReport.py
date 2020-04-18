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
        self.from_word = self.report.from_word
        self.from_excel = self.report.from_excel
        self.target_word = self.from_word.replace("fromEndStr", "20200305-20200306")
        self.target_excel = self.from_excel.replace("fromEndStr", "20200305-20200306")
        self.from_dir = self.report.get_from_dir()
        self.date_tuple = (datetime.date(2020, 3, 5), datetime.date(2020, 3, 6))

    def test_1_copy_word_file(self):
        self.report.copy_file(self.from_word, self.target_word)
        assert os.path.exists(os.path.join(self.from_dir, self.target_word)) is True

    def test_2_replace_date_str(self):
        content = "lslldf from_end_str"
        assert (
            self.report.replace_date_str(content, "from_end_str", "20200305-20200306")
            == "lslldf 20200305-20200306"
        )

    def test_4_copy_excel(self):
        self.report.copy_file(self.from_excel, self.target_excel)
        assert os.path.exists(os.path.join(self.from_dir, self.target_excel)) is True

    def test_5_check_and_change(self):
        self.report.check_word_change(self.target_word, self.date_tuple)

    def test_9_check_excel_change(self):
        self.report.check_excel_change(self.target_excel, self.date_tuple)

    def tearDown(self):
        print("tearDown...")


if __name__ == "__main__":
    unittest.main()
