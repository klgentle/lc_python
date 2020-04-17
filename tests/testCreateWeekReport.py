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
        self.target_file = os.path.join(
            self.report.from_dir,
            self.report.from_file.replace("fromEndStr", "20200305-20200306"),
        )
        self.target_file2 = os.path.join(
            self.report.from_dir,
            self.report.from_file.replace("fromEndStr", "20200305-20200306_"),
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
        document = docx.Document(self.target_file)
        document = self.report.check_word_change(document, date_tuple)
        document.save(self.target_file)
        # 无法 assert 只能肉眼看 

    def tearDown(self):
        print("tearDown...")


if __name__ == "__main__":
    unittest.main()
