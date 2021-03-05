"""
556. Next Greater Element III
Medium

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21

Example 2:

Input: n = 21
Output: -1

"""

from itertools import permutations

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        ms = list(str(n))
        res = 2**31

        for m in permutations(ms, len(ms)):
            v = int("".join(m))
            #print(v)
            if v > n and v <= 2**31 - 1:
                res = min(res, v)

        if res != 2**31:
            return res
        else:
            return -1
