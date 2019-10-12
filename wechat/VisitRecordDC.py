# py3.7


@dataclass(unsafe_hash=True)
class VisitRecordDC(object):
    first_name: str
    last_name: str
    phone_number: str
    # 跳过“访问时间”字段，不作为任何对比条件
    date_visited: str = field(hash=False, compare=False)

    def find_potential_customers_v4():
        return set(VisitRecordDC(**r) for r in users_visited_puket) - set(
            VisitRecordDC(**r) for r in users_visited_nz
        )



if __name__ == "__main__":
    # 去过普吉岛的人员数据
    users_visited_puket = [ { "first_name" : "Sirena" , "last_name" : "Gross" , "phone_number" : "650-568-0388" , "date_visited" : "2018-03-14" }, { "first_name" : "James" , "last_name" : "Ashcraft" , "phone_number" : "412-334-4380" , "date_visited" : "2014-09-16" }, ] 
    # 去过新西兰的人员数据 
    users_visited_nz = [ { "first_name" : "Justin" , "last_name" : "Malcom" , "phone_number" : "267-282-1964" , "date_visited" : "2011-03-13" }, { "first_name" : "Albert" , "last_name" : "Potter" , "phone_number" : "702-249-3714" , "date_visited" : "2013-09-11" } ]
    obj = VisitRecordDC()
    print(obj.find_potential_customers_v4())
