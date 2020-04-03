
import datetime
import CheckInForm

"""
根据工作日期，生成周报模板
"""

class CreateWeekReport(object):
    def __init__(self):
        pass
    
    def get_all_weekday_interval(self, weekday_list:list) -> list :
        """
        返回每个时间区间构成的列表,如 [(date'2020-03-07',date'2020-03-07')]
        weekday_list:[datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),datetime.date(2020, 3, 7),datetime.date(2020, 3, 10),datetime.date(2020, 3, 13),datetime.date(2020, 3, 14)]
        
        """
        pre_date = None
        interval_start = None
        interval_end = None
        interval = []
        for date in weekday_list:
            if pre_date is None:
                interval_start = date        
            elif date == pre_date + datetime.timedelta(1):
                interval_end = date
            else:
                interval.append((interval_start, interval_end))
                interval_start = date        
                interval_end = date
                
            pre_date = date
            
        print("result:", interval)
        return interval



if __name__ == "__main__":
    obj = CreateWeekReport()
    weekday_list1 = [datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),datetime.date(2020, 3, 7)]
    print(weekday_list1)
    assert obj.get_all_weekday_interval(weekday_list1) == [(datetime.date(2020, 3, 5),datetime.date(2020, 3, 7))]

    weekday_list = [datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),datetime.date(2020, 3, 7),datetime.date(2020, 3, 10),datetime.date(2020, 3, 13),datetime.date(2020, 3, 14)]
    print(weekday_list)
    assert obj.get_all_weekday_interval(weekday_list) == [(datetime.date(2020, 3, 5),datetime.date(2020, 3, 7)),(datetime.date(2020, 3, 10),datetime.date(2020, 3, 10)), (datetime.date(2020, 3, 13), datetime.date(2020, 3, 14))]
