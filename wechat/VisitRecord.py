class VisitRecord:
    """旅游记录 """

    def __init__(self, first_name, last_name, phone_number, date_visited):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_visited = date_visited

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.phone_number))

    def __eq__(self, other):
        # 当两条访问记录的名字与电话号相等时，判定二者相等。
        if isinstance(other, VisitRecord) and hash(other) == hash(self):
            return True
        return False

    def find_potential_customers_v3():
        return set(VisitRecord(**r) for r in users_visited_puket) - set(
            VisitRecord(**r) for r in users_visited_nz
        )
