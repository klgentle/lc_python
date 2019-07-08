
import datetime


def date_add(day: int) -> str:
    date=datetime.date.today()+datetime.timedelta(days=day)
    return date.strftime("%Y%m%d")
