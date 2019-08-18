"""
fix records:
1. end date is 2019/8/16
2. add while, date input format
3. pd.contact -> pd.concat([df1, df2])
"""
import pandas as pd


from_date = "2018/1/17"
to_date = "2019/8/16"

# for test start = "2018-03-20"
start = input("Enter the beginning date between 2018-1-17 and 2019-8-16: ")
start_list = start.split("-")
# date format
start_date = (
    start_list[0] + "/" + str(int(start_list[1])) + "/" + str(int(start_list[2]))
)
# print(start_date)
while start_date < from_date or start_date > to_date:
    print("Start date is out of the date range")
    start = input("Enter the beginning date between 2018-1-17 and 2019-8-16: ")
    start_list = start.split("-")
    # date format
    start_date = (
        start_list[0] + "/" + str(int(start_list[1])) + "/" + str(int(start_list[2]))
    )

# for test end = '2018-08-16'
end = input("Enter the ending date between 2018-1-17 and 2019-8-16: ")
end_list = end.split("-")
# date format
end_date = end_list[0] + "/" + str(int(end_list[1])) + "/" + str(int(end_list[2]))
# print(start_date)
while end_date < start_date or end_date > to_date:
    if end_date < start_date:
        print("End date cannot be before start date")
    else:
        print("End date is out of the date range")
    end = input("Enter the ending date between 2018-1-17 and 2019-8-16: ")
    end_list = end.split("-")
    # date format
    end_date = end_list[0] + "/" + str(int(end_list[1])) + "/" + str(int(end_list[2]))


print("Summary of stock prices from", start, "to", end)
CMG = pd.read_csv("CMG.csv")
COKE = pd.read_csv("COKE.csv")
NKE = pd.read_csv("NKE.csv")
# add Symbol for stock to mark
length = len(CMG["Date"])
CMG["Symbol"] = ["CMG"] * length
COKE["Symbol"] = ["COKE"] * length
NKE["Symbol"] = ["NKE"] * length

all_data = pd.concat([CMG, COKE, NKE])
all_data["Date"] = pd.to_datetime(all_data["Date"])  # 将数据类型转换为日期类型
all_data = all_data.set_index("Date")  # 将date设置为index
select = all_data.loc[start:end, ["Adj Close", "Symbol"]]

# rename column for agg
select = select.rename({"Adj Close": "Adj_Close"}, axis="columns")

# get the begin data
begining_price = select.loc[start:start, ["Adj_Close", "Symbol"]]
# get the end data
ending_price = select.loc[end:end, ["Adj_Close", "Symbol"]]
# transfer into group by for join
begin_group = begining_price.groupby("Symbol").max()
end_group = ending_price.groupby("Symbol").max()

# rename column for display
begin_group = begin_group.rename({"Adj_Close": "Begining Price"}, axis="columns")
end_group = end_group.rename({"Adj_Close": "Ending Price"}, axis="columns")

# data format for display
pd.options.display.float_format = "{:,.2f}".format
stock_out = pd.DataFrame(select.groupby("Symbol").Adj_Close.agg(["min", "max", "mean"]))
# rename column for display
stock_out = stock_out.rename(
    {"min": "Minimum", "max": "Maximum", "mean": "Average"}, axis="columns"
)
stock_out = pd.concat([begin_group, end_group, stock_out], axis="columns")
print(stock_out)
