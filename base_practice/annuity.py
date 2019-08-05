month=0
investment=int(input("Please enter your initial investment: "))
rate=float(input("Please enter annual interest rate(ex. 2.5): "))
payout=int(input("Please enter the monthly annuity payout: "))

rate = rate / 100
balance=investment
#balance=investment-payout/rate*(1-1/(1+rate/12)**month)
if payout>=investment:
    print("After", month,"months","your balance is {0:.2f}.".format(balance))
else:
    while balance >=payout:
        balance = balance * (1+ rate/12) - payout
        print(f"balance:{balance}")
        month+=1
        print(f"month:{month}")
    print("After", month,"months","your balance is {0:.2f}.".format(balance))
