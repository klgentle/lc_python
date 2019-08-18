import pandas as pd
loan=pd.read_csv('loan.csv')
loan50=loan[(loan['Bo_Age']>50)]
print(loan50['Cust_ID'].groupby(loan50['OUTCOME']).count(),'\n\n\n')
print(loan50.groupby(loan50['OUTCOME']).mean())

#loan1=loan[(loan['Bo_Age']>50) & (loan['OUTCOME']=='default')]
#print(loan1.head())
#loan2=loan[(loan['Bo_Age']>50) & (loan['OUTCOME']=='non-default')]
#print(loan2.head())

