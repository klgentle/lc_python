import matplotlib.pyplot as plt
import pandas as pd
import requests


def get_stock():
    # 选择要获取的时间段
    periods = "3600"

    # 通过Http抓取btc历史价格数据
    resp = requests.get(
        "https://api.cryptowat.ch/markets/gemini/btcusd/ohlc",
        params={"periods": periods},
    )

    data = resp.json()

    # 转换成pandas data frame
    df = pd.DataFrame(
        data["result"][periods],
        columns=["CloseTime", "OpenPrice", "HighPrice", "LowPrice", "ClosePrice", "Volume", "NA"],
    )

    # 输出DataFrame的头部几行
    print(df.head())

    print("to show plot ------------------")
    # 绘制btc价格曲线
    df["ClosePrice"].plot(figsize=(14, 7))
    plt.show()


if __name__ == "__main__":
    get_stock()
