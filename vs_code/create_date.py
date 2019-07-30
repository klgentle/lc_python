import datetime
def getBetweenDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y%m%d")
    #print(f"begin_date:{begin_date}")
    end_date = datetime.datetime.strptime(end_date, "%Y%m%d")
    #print(f"end_date:{end_date}")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y%m%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    #print(f"date_list:{date_list}")
    return date_list


if __name__ == '__main__':
    getBetweenDay('20190725','20190730')
