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
from automatic_office.DealInterval import DealInterval

class testDealInterval(unittest.TestCase):
    def setUp(self):
        print("setUp...")
        self.report = DealInterval()
        self.date_tuple = (datetime.date(2020, 3, 5), datetime.date(2020, 3, 7))

    def test_get_from_end_str(self):
        assert self.report.get_from_end_str(self.date_tuple) == "20200305-20200307"

    def test_get_from_date(self):
        assert self.report.get_from_date(self.date_tuple) == "2020-03-05"

    def test_get_end_date(self):
        assert self.report.get_end_date(self.date_tuple) == "2020-03-07"

    def test_get_one_weekday_interval(self):
        weekdays = [
            datetime.date(2020, 3, 5),
            datetime.date(2020, 3, 6),
            datetime.date(2020, 3, 7),
        ]
        print("weekdays1", weekdays)
        assert self.report.get_all_weekday_interval(weekdays, []) == [
            (datetime.date(2020, 3, 5), datetime.date(2020, 3, 7))
        ]

    def test_get_two_weekday_interval(self):
        weekdays = [
            datetime.date(2020, 3, 5),
            datetime.date(2020, 3, 6),
            datetime.date(2020, 3, 7),
            datetime.date(2020, 3, 13),
            datetime.date(2020, 3, 14),
        ]
        print("weekdays2", weekdays)
        print("out2")
        out = self.report.get_all_weekday_interval(weekdays, [])
        pprint.pprint(out)
        assert out == [
            (datetime.date(2020, 3, 5), datetime.date(2020, 3, 7)),
            (datetime.date(2020, 3, 13), datetime.date(2020, 3, 14)),
        ]

    def test_get_three_weekday_interval_with_oneday_separate(self):
        weekdays = [
            datetime.date(2020, 3, 5),
            datetime.date(2020, 3, 6),
            datetime.date(2020, 3, 7),
            datetime.date(2020, 3, 10),
            datetime.date(2020, 3, 13),
            datetime.date(2020, 3, 14),
        ]
        print("weekdays3", weekdays)
        out3 = self.report.get_all_weekday_interval(weekdays, [])
        print("out3", out3)
        assert out3 == [
            (datetime.date(2020, 3, 5), datetime.date(2020, 3, 7)),
            (datetime.date(2020, 3, 10), datetime.date(2020, 3, 10)),
            (datetime.date(2020, 3, 13), datetime.date(2020, 3, 14)),
        ]

    def tearDown(self):
        print("tearDown...")


if __name__ == "__main__":
    unittest.main()
