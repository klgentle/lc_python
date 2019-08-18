"""
fix records:
1. end date is 2019/8/16
2. add while, date input format
3. pd.contact -> pd.concat([df1, df2])
"""
import pandas as pd


from_date = "2018/1/17"
to_date = "2019/8/16"

start = "2018-03-20" 
#start = input("Enter the beginning date between 2018-1-17 and 2019-8-16: ")
start_list = start.split("-")
# date format
start_date = start_list[0] + "/" + str(int(start_list[1])) + "/" + str(int(start_list[2]))
# print(start_date)
while start_date < from_date or start_date > to_date:
    print("Start date is out of the date range")
    start = input("Enter the beginning date between 2018-1-17 and 2019-8-16: ")
    start_list = start.split("-")
    # date format
    start_date = start_list[0] + "/" + str(int(start_list[1])) + "/" + str(int(start_list[2]))

end = '2018-08-16'
#end = input("Enter the ending date between 2018-1-17 and 2019-8-16: ")
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
# add Symbol for stock
length = len(CMG['Date'])
CMG['Symbol'] = ['CMG'] * length
COKE['Symbol'] = ['COKE'] * length
NKE['Symbol'] = ['NKE'] * length

all_data = pd.concat([CMG, COKE, NKE])
all_data['Date'] = pd.to_datetime(all_data['Date']) #将数据类型转换为日期类型
all_data = all_data.set_index('Date') # 将date设置为index
#print(all_data.head())
select=all_data.loc[start:end,['Adj Close', 'Symbol']]

print(select['Adj Close'].groupby(select['Symbol']).mean().head())

df1 = pd.DataFrame(select.groupby(select['Symbol']).mean())

#df2 = pd.DataFrame(select.groupby(select['Symbol']).min().reset_index(),  columns=['Minimum'])   #'Symbol',
df2 = pd.DataFrame(select.groupby(select['Symbol']).min())
print("df2",df2)
df3 = pd.DataFrame(select.groupby(select['Symbol']).max())
print("df3",df3)
df_out = pd.merge(df1,df2,df3)

print("merge_df",merge_df)

#print(loan50['Cust_ID'].groupby(loan50['OUTCOME']).count(),'\n\n\n')
#print(loan50.groupby(loan50['OUTCOME']).mean())

