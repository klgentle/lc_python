import sqlite3


def demo():
    # 若不存在则创建
    con = sqlite3.connect("test.db")
    # 游标对象
    cur = con.cursor()
    # 新建表
    cur.execute(
        "create table if not exists ifrs9_data \
         (site_name text primary key not null, ind int, file_info text, path_name text, record_count int)"
    )
    # insert data
    cur.execute(
        "INSERT INTO ifrs9_data(site_name, ind, file_info, path_name, record_count) VALUES(?,?,?,?,?)",
        ("AMH", 1, "12312 Oct 22 22:22", "name.sf", 123),
    )
    cur.execute(
        "INSERT INTO ifrs9_data(site_name, ind, file_info, path_name, record_count) VALUES(?,?,?,?,?)",
        ("HSCN", 1, "21312 Oct 22 22:22", "name.sf", 213),
    )
    cur.execute("select * from ifrs9_data")
    print(cur.fetchall())

    con.commit()
    con.close()

    pass


if __name__ == "__main__":
    demo()
