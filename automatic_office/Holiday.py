import json
import requests


class Holiday(object):
    def api_holiday(self, date_str: str) -> int:
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
        api_url = r"http://www.easybots.cn/api/holiday.php?d={}".format(
            date_str
        )
        r = requests.get(api_url)
        resp = json.loads(r.text)
        # test
        #print(resp)
        #工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2
        return resp.get(date_str) in ("1", "2")

    def is_holiday(self, date_str: str) -> bool:
        return self.api_holiday(date_str)


if __name__ == "__main__":
    obj = Holiday()
    # print(obj.api_holiday("20190929"))
    print(obj.is_holiday("20191126"))
    print(obj.is_holiday("20191221"))
    print(obj.is_holiday("20200101"))
