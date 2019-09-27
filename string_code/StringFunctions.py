class StringFunctions(str):

    def __init__(self, string: str):
        self = string

    def find_the_second_position(self, target_str: str) -> int:
        target_str_ind = self.find(target_str)
        if target_str_ind == -1:
            return -1
        target_str_ind_and_len = target_str_ind+len(target_str)
        str_last = self[target_str_ind_and_len:]
        if str_last.find(target_str) == -1:
            return -1
        return target_str_ind_and_len + str_last.find(target_str)

    def str_insert(self, position: int, add_str: str) -> str:
        "insert in assign point"
        return self[0:position] + add_str + self[position:]


if __name__ == '__main__':
    a = StringFunctions('AND a =b AND c=d')
    postion = a.find_the_second_position('AND')
    print(postion)
    print(a.str_insert(postion, '\n'))
