from data_base_connect import connect
#import cx_Oracle

# use in linux or centos, not in windos (libclntsh.so: cannot open shared object file: No such file or directory)
#conn = cx_Oracle.connect('rptuser', 'rptuser','100.11.94.176:1521/odsdb')
conn = connect()
cursor = conn.cursor()
cursor.execute("select id from rpt_account_mid where data_date != date'2018-08-30'")

#result = cursor.fetchall()
#for row in result:
#    print(row[0])
result = cursor.fetchone()
print(result[0])


cursor.close()
conn.close()
