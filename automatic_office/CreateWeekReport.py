
import datetime
import CheckInForm
import pysnooper

"""
根据工作日期，生成周报模板
"""

class CreateWeekReport(object):
    def __init__(self):
        pass
    
    @pysnooper.snoop()
    def get_all_weekday_interval(self, weekdays:list, intervals=[]) -> list :
        """
        返回每个时间区间构成的列表,如 [(date'2020-03-07',date'2020-03-07')]
        weekdays:[datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),datetime.date(2020, 3, 7),datetime.date(2020, 3, 10),datetime.date(2020, 3, 13),datetime.date(2020, 3, 14)]
        
        """
        if len(weekdays) == 1:
            return intervals.append((weekdays[0], weekdays[0]))
        elif len(weekdays) <= 0:
            return intervals

        for i, date in enumerate(weekdays):
            if weekdays[i+1] == date + datetime.timedelta(1):
                continue
            else:
                intervals.append((weekdays[0], weekdays[-1]))
                return self.get_all_weekday_interval(weekdays[i+1:], intervals)


if __name__ == "__main__":
    obj = CreateWeekReport()
    weekdays1 = [datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),datetime.date(2020, 3, 7)]
    print(weekdays1)
    assert obj.get_all_weekday_interval(weekdays1) == [(datetime.date(2020, 3, 5),datetime.date(2020, 3, 7))]

    #weekdays = [datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),datetime.date(2020, 3, 7),datetime.date(2020, 3, 10),datetime.date(2020, 3, 13),datetime.date(2020, 3, 14)]
    #print(weekdays)
    #assert obj.get_all_weekday_interval(weekdays) == [(datetime.date(2020, 3, 5),datetime.date(2020, 3, 7)),(datetime.date(2020, 3, 10),datetime.date(2020, 3, 10)), (datetime.date(2020, 3, 13), datetime.date(2020, 3, 14))]
