"""
1.分析可转债近一年收益情况，如果按海哥的策略(现价/转股价>= 96%)，一年单账户可以获利多少
2.需要准备多少资金，
3.如果修改策略单账户最多获利多少，
4.一个人最多可以申请几个账户
5.理论上一个人动用多个账户一年最多可以赚多少?
"""
import pandas as pd
import pandas_datareader.data as web
import time


class ConvertibleBondAnalysis(object):
    def __init__(self):
        self._bond_data = pd.read_csv("convertibile_bond.csv", "GB2312")
        #self.set_open_price()
        #self._bond_data_with_price = pd.read_csv("convertibile_bond_with_price.csv", "GB2312")

    @staticmethod
    def date_change_format(from_date: str) -> str:
        """
        from_date: %Y/%m/%d
        out: %Y-%m-%d
        """
        input_date = time.strptime(from_date, "%Y/%m/%d")
        return time.strftime("%Y-%m-%d", input_date)

    def get_bond_open_value(self, code: str, open_date: str) -> int:
        # open_date format "2017-01-01"
        bond_data = web.get_data_yahoo(code, open_date, open_date)
        # print(bond_data.head())
        # 取第一天开板价格
        return bond_data.loc[open_date, "Open"]

    def set_open_price(self):
        self._bond_data["open_price"] = [
            self.get_bond_open_value(
                self._bond_data.iloc[i][0],  #bond_code
                self.date_change_format(self._bond_data.iloc[i][9]),  #open_date
            )
            for i in self._bond_data.index
        ]
        self._bond_data.to_csv(
            "./convertibile_bond_with_price.csv", sep=",", header=True
        )

    def test_data_detect(self):
        #print(self._bond_data.head())
        print(self._bond_data.iloc[2])
        print(type(self._bond_data.iloc[2]))
        print("-------------", self._bond_data.iloc[2][0])

    def test_data_detect2(self):
        print(self._bond_data_with_price.head())
        print(self._bond_data_with_price.index)

    def test_data_index(self):
        for i in self._bond_data.index:
            print(i)


if __name__ == "__main__":
    obj = ConvertibleBondAnalysis()
    # 用正股价格去推算可转债上市价格
    # obj.get_bond_open_value("601818.ss", "2017-04-05")
    # print(obj.date_change_format("2017/4/5"))
    #obj.test_data_index()
    #obj.test_data_detect2()
    obj.test_data_detect()
