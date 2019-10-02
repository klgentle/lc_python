import json
import requests


class Holiday(object):
    def api_holiday(self, date_str: str) -> int:
        """
        argv:
            date_str:yyyymmdd

        > 返回数据：正常工作日对应结果为 0, 
                   节假日调休补班对应的结果为 2，
                   法定节假日对应结果为 1, 
                   休息日对应结果为 3 
        > 示例： 
        http://api.goseek.cn/Tools/holiday?date=20170528 
        > 返回数据： 
        {"code":10000,"data":1}
        """
        api_url = r"http://api.goseek.cn/Tools/holiday?date={}".format(
            date_str)
        r = requests.get(api_url)
        resp = json.loads(r.text)
        return resp.get('data')

    def is_holiday(self, date_str: str) -> bool:
        return self.api_holiday(date_str) % 2 == 1


if __name__ == "__main__":
    obj = Holiday()
    # print(obj.api_holiday("20190929"))
    print(obj.is_holiday("20190929"))
    print(obj.is_holiday("20190930"))
