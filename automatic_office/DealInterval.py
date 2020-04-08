import datetime
#import pysnooper
#import pprint
import os
import sys


# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

"""
根据工作日期，生成周报模板
"""


class DealInterval(object):
    def __init__(self):
        pass

    @staticmethod
    def get_from_end_str(date_tuple: tuple) -> str:
        """
        date_tuple: (datetime.date(2020, 3, 5), datetime.date(2020, 3, 7))
        """
        return "-".join(
            [
                datetime.datetime.strftime(date_tuple[0], "%Y%m%d"),
                datetime.datetime.strftime(date_tuple[1], "%Y%m%d"),
            ]
        )

    @staticmethod
    def get_from_date(date_tuple: tuple) -> str:
        return datetime.datetime.strftime(date_tuple[0], "%Y-%m-%d")

    @staticmethod
    def get_end_date(date_tuple: tuple) -> str:
        return datetime.datetime.strftime(date_tuple[1], "%Y-%m-%d")

    # @pysnooper.snoop()
    def get_all_weekday_interval(self, weekdays: list, intervals=[]) -> list:
        # 查看一下，为什么默认值没有显示设置为空，结果会变？
        """
        返回每个时间区间构成的列表,如 [(date'2020-03-07',date'2020-03-07')]
        weekdays:[datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),
                  datetime.date(2020, 3, 7),datetime.date(2020, 3, 10),
                  datetime.date(2020, 3, 13),datetime.date(2020, 3, 14)]
        """
        if len(weekdays) == 1:
            intervals.append((weekdays[0], weekdays[0]))
            return intervals
        elif len(weekdays) <= 0:
            return intervals

        for i, date in enumerate(weekdays):
            # print(f"i:{i}, date:{date}")
            # pprint.pprint("intervals:%s" % intervals)
            # 如果是最后一个
            if i == len(weekdays) - 1:
                intervals.append((weekdays[0], weekdays[-1]))
                return intervals

            if weekdays[i + 1] == date + datetime.timedelta(1):
                continue
            else:
                intervals.append((weekdays[0], date))
                return self.get_all_weekday_interval(weekdays[i + 1 :], intervals)


if __name__ == "__main__":
    obj = DealInterval()
