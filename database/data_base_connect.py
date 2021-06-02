import cx_Oracle


def connect(da_name="171"):
    conn = cx_Oracle.connect('rptuser', 'rptuser','100.11.94.176:1521/odsdb')
    return conn

