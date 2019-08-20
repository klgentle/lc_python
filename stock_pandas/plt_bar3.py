import matplotlib.pyplot as plt
import pandas as pd

# x 是x轴，y是height，
loan = pd.read_csv("loan.csv")

# 单列时sort不用写by
x = loan["Credit_score"].drop_duplicates().sort_values()
#print(x)
y = loan["Credit_score"].groupby(loan["Credit_score"]).count()
#print(y)
#x = [625, 650, 675, 700, 725, 750, 775, 800]
#y = [2.0, 2.0, 1.0, 3.0, 4.0, 2.0, 1.0, 2.0]
p1 = plt.bar(x, height=y, width=2)
plt.title("Credit_score")
plt.grid(axis='y')
plt.grid(axis='x')
plt.show()
