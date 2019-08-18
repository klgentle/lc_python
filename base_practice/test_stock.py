import unittest
from stock_anal import date_start_input


class MyTestCase(unittest.TestCase):
    def test_input(self):
        self.assertEqual(date_start_input("2014-08-08"), "Start date is out of the date range")
        self.assertEqual(date_start_input("2019-09-08"), "Start date is out of the date range")
        self.assertEqual(date_start_input("2019-08-08"), None)
        print(date_start_input("2019-09-08"))


if __name__ == '__main__':
    unittest.main()
