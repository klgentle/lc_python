from typing import List


class Solution(object):
    """
    二进制数可以分成两部分:
    一部分是最后一位 (i&1), 另一部分是除最后一位的其他部分 (i >> 1)
    1 =    1
    2 =   10
    3 =   11
    4 =  100
    5 =  101
    6 =  110
    7 =  111
    8 = 1000
    """

    def countBits(self, num: List[int]) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            res += (res[i >> 1] + (i & 1),)
        return res


if __name__ == "__main__":
    print(Solution().countBits(4))
