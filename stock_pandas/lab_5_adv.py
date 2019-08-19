import pandas as pd

loan = pd.read_csv("loan.csv")
keepgoing = "Y"
while keepgoing == "Y":
    variable = input("Enter variable:")
    comparison = input("Enter comparison >,<,= : ")
    value = input("Enter value of cutoff:")
    # todo TypeError: Invalid comparison between dtype=int64 and str
    if value.isdigit():
        value = int(value)
    # reverse comparison and delete rows
    if comparison == ">":
        loan = loan[loan[variable] <= value]
    elif comparison == "<":
        loan = loan[loan[variable] >= value]
    elif comparison == "=":
        loan = loan[loan[variable] != value]

    keepgoing = input("Do you want to slice by another variable (Y for yes?):")

print(loan.head(10))
print(loan.describe(include="all"))
