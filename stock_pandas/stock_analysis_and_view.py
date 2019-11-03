"""
数据可视化：股票数据分析
"""

import pandas as pd
from pandas_datareader import data


'''
获取国内股票数据的方式是：“股票代码”+“对应股市”（港股为.hk，A股为.ss）
例如腾讯是港股是：0700.hk
'''
#字典：6家公司的股票
gafataDict={'谷歌':'GOOG','亚马逊':'AMZN','Facebook':'FB',
            '苹果':'AAPL','阿里巴巴':'BABA','腾讯':'0700.hk'}


'''
get_data_yahoo表示从雅虎数据源获取股票数据，官网使用操作文档：
http://pandas-datareader.readthedocs.io/en/latest/remote_data.html
可能存在的问题：
1）由于是从国外获取股票数据，会由于网络不稳定，获取数据失败，多运行几次这个cell就好了
2）如果多运行几次还是无法获的股票数据，使用这个链接里的方法：https://pypi.org/project/fix-yahoo-finance/0.0.21/
3）如果经过上面2个方法还不行，打开这个官网使用文档（http://pandas-datareader.readthedocs.io/en/latest/remote_data.html），
换其他的财经数据源试试
'''
# 获取哪段时间范围的股票数据
start_date = '2017-01-01'
end_date = '2018-01-01'
#从雅虎财经数据源（get_data_yahoo）获取阿里巴巴股票数据
babaDf=data.get_data_yahoo(gafataDict['阿里巴巴'],start_date, end_date)
#或者从Morningstar数据源获取阿里巴巴数据
#babaDf=data.DataReader(gafataDict['阿里巴巴'],'morningstar',start_date, end_date)

#查看前5行数据
babaDf.head()
