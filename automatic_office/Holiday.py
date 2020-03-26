import json
import requests
import os
from datetime import datetime


class Holiday(object):
    def is_holiday(self, date_str: str) -> bool:
        """
        date_str: YYYYmmdd

        周末上班对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2
        不上班有两种情况：
        1: josn data is 1 or 2
        2: weekend and josn data not equal to 0
        """
        year = date_str[0:4]
        day = date_str[4:]  # ddmm
        with open(os.path.join("data","{}_data.json".format(year))) as f:
            data = json.loads(f.read())

        # 国家规定上班与放假的情况
        if data.get(day) in (1, 2):
            return True
        elif data.get(day) == 0:
            return False

        # 周末不上班的情况
        date = datetime.strptime(date_str, "%Y%m%d").date()
        if date.weekday() in (5, 6):
            return True
        else:
            return False

    def api_holiday_not_used(self, date_str: str) -> bool:
        """
        argv:
            date_str:yyyymmdd
        > 示例： 
        --http://api.goseek.cn/Tools/holiday?date=20170528 
        --http://timor.tech/api/holiday/info/2019-11-26
        http://www.easybots.cn/api/holiday.php?d=
        > 返回数据： 
        "20200101":"2"
        """
        api_url = r"http://www.easybots.cn/api/holiday.php?d={}".format(date_str)
        r = requests.get(api_url)
        resp = json.loads(r.text)
        # test
        # print(resp)
        # 工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2
        return resp.get(date_str) in ("1", "2")

    def is_holiday_not_used(self, date_str: str) -> bool:
        return self.api_holiday(date_str)


if __name__ == "__main__":
    obj = Holiday()
    # print(obj.api_holiday("20190929"))
    print(obj.is_holiday("20200101"))
    print(obj.is_holiday("20200130"))
    print(obj.is_holiday("20200119"))
    print(obj.is_holiday("20200118"))
    print(obj.is_holiday("20200112"))
