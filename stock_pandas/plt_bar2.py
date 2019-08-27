import matplotlib.pyplot as plt
import pandas as pd

# x 是x轴，y是y轴，
loan = pd.read_csv("loan.csv")

x = loan["Credit_score"]
y = loan["Credit_score"].groupby(loan["Credit_score"]).count()
#print(f"x:{x}")
#print(f"y:{y}")
#x = [625, 650, 675, 700, 725, 750, 775, 800]
#y = [2.0, 2.0, 1.0, 3.0, 4.0, 2.0, 1.0, 2.0]
p1 = plt.bar(x.drop_duplicates(), height=y, width=10)
plt.title("Credit_score")
plt.grid(axis='y')
plt.grid(axis='x')
plt.show()
