import sqlite3


def demo(site_name):
    # 若不存在则创建
    con = sqlite3.connect("ifrs9.db")
    # 游标对象
    cur = con.cursor()
    # 新建表
    cur.execute(
        "create table if not exists ifrs9_data \
         (site_name text primary key not null, data text)"
    )
    cur.execute(
        "delete from ifrs9_data where site_name=?", (site_name,)
    )
    # insert data
    cur.execute(
        "INSERT INTO ifrs9_data(site_name, data) VALUES(?,?)",
        ("HASE", "1,HASE,12312,Oct,22,22:46,123\n2,HSCN,12312,Oct,22,22:46,123\n3,HMO,12312,Oct,22,22:46,123"),
    )
    cur.execute("select * from ifrs9_data")
    print(cur.fetchall())

    con.commit()
    con.close()

    pass


if __name__ == "__main__":
    demo("HASE")
