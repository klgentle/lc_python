
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
        weekday_list:[datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),datetime.date(2020, 3, 7),datetime.date(2020, 3, 10),datetime.date(2020, 3, 13),datetime.date(2020, 3, 14)]
        
        """
        pre_date = None
        interval_start = None
        interval_end = None
        interval = []
        for date in weekday_list:
            if pre_date = None:
                interval_start = date        
            elif date = pre_date + datetime.timedelta(1)
                pass
            pre_date = date
            



if __name__ == "__main__":
    obj = CreateWeekReport()
    weekday_list = [datetime.date(2020, 3, 5), datetime.date(2020, 3, 6),datetime.date(2020, 3, 7),datetime.date(2020, 3, 10),datetime.date(2020, 3, 13),datetime.date(2020, 3, 14)]
    assert obj.get_all_weekday_interval(weekday_list) = [(datetime.date(2020, 3, 5),datetime.date(2020, 3, 7)),(datetime.date(2020, 3, 10),datetime.date(2020, 3, 10)), (datetime.date(2020, 3, 13), datetime.date(2020, 3, 14))]
