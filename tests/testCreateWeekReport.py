import os
import sys
from os.path import dirname
import datetime
import pprint
import unittest

# 项目根目录
BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
# 添加系统环境变量
sys.path.append(BASE_DIR)
from automatic_office.CreateWeekReport import CreateWeekReport


class testCreateWeekReport(unittest.TestCase):
    def setUp(self):
        print("setUp...")
        self.report = CreateWeekReport("202003")

    def test_copy_file(self):
        self.report.copy_file("20200305-20200306")
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)) + "/../",
            "automatic_office",
            "doc_file",
            "创兴银行香港ODS项目周报_董坚_20200305-20200306.docx",
        )
        assert os.path.exists(file_path) is True

    def test_replace_date_str(self):
        content = "lslldf from_end_str"
        assert self.report.replace_date_str(content,"from_end_str","20200305-20200306") == "lslldf 20200305-20200306"

        

    def tearDown(self):
        print("tearDown...")


if __name__ == "__main__":
    unittest.main()
