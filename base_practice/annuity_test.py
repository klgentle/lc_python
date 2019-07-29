month=0
investment=10000 #int(input("Please enter your initial investment: "))
rate=3.6 #float(input("Please enter annual interest rate(ex. 2.5): "))
payout=600 #int(input("Please enter the monthly annuity payout: "))

rate = rate /100
if payout>=investment:
    print("After", month,"months","your balance is {}.".format(investment,'.2f'))
else:
    #balance=investment-payout/rate*(1-1/(1+rate/12)**month)
    balance=investment-payout*(1+rate/12)**month
    while balance >=payout:
        balance=investment-payout*(1+rate/12)**month
        print(f"balance:{balance}")
        month+=1
        print(f"month:{month}")
    print("After", month,"months","your balance is {}.".format(balance,'.2f'))
