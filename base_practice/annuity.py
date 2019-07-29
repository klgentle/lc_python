month=0
investment=int(input("Please enter your initial investment: "))
rate=float(input("Please enter annual interest rate(ex. 2.5): "))
rate = rate /100
payout=int(input("Please enter the monthly annuity payout: "))

if payout>=investment:
    print("After", month,"months","your balance is {}.".format(investment,'.2f'))
else:
    balance=investment-payout/rate*(1-1/(1+rate/12)**month)
    while balance >=payout:
        balance=investment-payout/rate*(1-1/(1+rate/12)**month)
        print(f"balance:{balance}")
        month+=1
        print(f"month:{month}")
    print("After", month,"months","your balance is {}.".format(balance,'.2f'))
