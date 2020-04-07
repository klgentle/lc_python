import sqlparse


def sqlFormat(sql: str) -> str:
    return sqlparse.format(sql, reindent=True, keyword_case='upper')


if __name__ == "__main__":
    sql = """select * from (select a, b, sum(c) from foo where d = 1 and e in ('a', 'b') group by f) t1 join (select a, g from bar) t2 on t1.a = t2.a left outer join t3 on t1.a = t3.a"""
    print(sqlFormat(sql))
