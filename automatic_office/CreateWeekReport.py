import datetime
import CheckInForm
import pysnooper
import pprint

"""
根据工作日期，生成周报模板
"""


class CreateWeekReport(object):
    def __init__(self):
        pass
    
    @staticmethod
    def get_from_end_str(date_tuple:tuple)->: str
        """
        date_tuple: (datetime.date(2020, 3, 5), datetime.date(2020, 3, 7))
        """
        return "-".join([datetime.datetime.strftime(date_tuple[0],'%Y%m%d'),
                         datetime.datetime.strftime(date_tuple[1],'%Y%m%d')])



    # @pysnooper.snoop()
    # 查看一下，为什么默认值没有显示设置为空，结果会变？
    def get_all_weekday_interval(self, weekdays: list, intervals=[]) -> list:
        """
        返回每个时间区间构成的列表,如 [(date'2020-03-07',date'2020-03-07')]
        weekdays:[datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),datetime.date(2020, 3, 7),datetime.date(2020, 3, 10),datetime.date(2020, 3, 13),datetime.date(2020, 3, 14)]
        
        """
        if len(weekdays) == 1:
            intervals.append((weekdays[0], weekdays[0]))
            return intervals
        elif len(weekdays) <= 0:
            return intervals

        for i, date in enumerate(weekdays):
            print(f"i:{i}, date:{date}")
            pprint.pprint("intervals:%s" % intervals)
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
    obj = CreateWeekReport()
    weekdays1 = [
       datetime.date(2020, 3, 5),
       datetime.date(2020, 3, 6),
       datetime.date(2020, 3, 7)
    ]
    print("weekdays1", weekdays1)
    assert obj.get_all_weekday_interval(weekdays1,[]) == [
       (datetime.date(2020, 3, 5), datetime.date(2020, 3, 7))
    ]

    #weekdays = [
    #    datetime.date(2020, 3, 5),
    #    datetime.date(2020, 3, 6),
    #    datetime.date(2020, 3, 7),
    #    datetime.date(2020, 3, 13),
    #    datetime.date(2020, 3, 14),
    #]
    #print("weekdays2", weekdays)
    #print("out2")
    #out = obj.get_all_weekday_interval(weekdays)
    #pprint.pprint(out)
    #assert out == [
    #    (datetime.date(2020, 3, 5), datetime.date(2020, 3, 7)),
    #    (datetime.date(2020, 3, 13), datetime.date(2020, 3, 14)),
    #]

    weekdays = [
       datetime.date(2020, 3, 5),
       datetime.date(2020, 3, 6),
       datetime.date(2020, 3, 7),
       datetime.date(2020, 3, 10),
       datetime.date(2020, 3, 13),
       datetime.date(2020, 3, 14)
    ]
    print("weekdays3", weekdays)
    out3 = obj.get_all_weekday_interval(weekdays,[])
    print("out3", out3)
    assert out3 == [
       (datetime.date(2020, 3, 5), datetime.date(2020, 3, 7)),
       (datetime.date(2020, 3, 10), datetime.date(2020, 3, 10)),
       (datetime.date(2020, 3, 13), datetime.date(2020, 3, 14))
    ]
