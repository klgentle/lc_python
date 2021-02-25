"""
710. Random Pick with Blacklist
Hard

Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

    1 <= N <= 1000000000
    0 <= B.length < min(100000, N)
    [0, N) does NOT include N. See interval notation.

"""

from random import randint

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        # new list：[0, white_len), [white_len, N). Focus on the last list
        self.white_len = N - len(blacklist)

        # new list 中小于white_len的blacklist会与大于white_len的非blacklist相对应
        keyToMove = [x for x in blacklist if x < self.white_len]
        valueToMatch = [x for x in range(self.white_len, N) if x not in blacklist]
        self.mapping = dict(zip(keyToMove, valueToMatch))


    def pick(self) -> int:
        i = randint(0, self.white_len-1)
        return self.mapping.get(i, i)


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
