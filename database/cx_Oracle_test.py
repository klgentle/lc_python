import cx_Oracle
conn = cx_Oracle.connect('rptuser', 'rptuser','100.11.94.176:1521/odsdb')
cursor = conn.cursor()
cursor.execute("select id from rpt_account_mid where data_date != date'2018-08-30'")

result = cursor.fetchall()
for row in result:
    print(row[0])

cursor.close()
conn.close()
