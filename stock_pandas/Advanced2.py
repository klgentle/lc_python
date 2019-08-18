Date=input("Enter a date between 8/8/2018 and 8/7/2019: ")
share1=int(input("Enter the number of shares of IBM:\n"))
share2=int(input("Enter the number of shares of MSFT:\n"))
#Date_str='3/29/2019'
#share1=4666
#share2=3222

date_list = Date_str.split('/')
Date = date_list[-1]+'/'+date_list[0]+'/' +date_list[1]
#print(Date)

#import datetime
#date_time = datetime.datetime.strptime(Date_str,'%m/%d/%Y')
#Date = date_time.strftime('%Y/%m/%d')

import pandas as pd
IBM=pd.read_csv('IBM.csv')
price1=float(IBM[(IBM['Date']==Date)]['Adj Close'])
#print(price1)
total1=price1*share1
#print(total1)

MSFT=pd.read_csv('MSFT.csv')
price2=float(IBM[(MSFT['Date']==Date)]['Adj Close'])
total2=price2*share2
total=total1+total2
print("Your portfolio report for:",Date)
print("The adjusted close price of IBM was:","$",price1,"and you had",share1)
print("The adjusted close price of MSFT was:","$",price2,"and you had",share2)
print("Your total portfolio value was ${:.2f}".format(total))
