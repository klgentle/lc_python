"""
438. Find All Anagrams in a String
Medium

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]
"""

class Solution:
    def findAnagrams(self, s: str, t: str) -> List[int]:
        """
        套用滑动窗口的框架，提前收缩窗口，这样可以保证进来的是目标字符的排列
        """
        need = {}
        wind = {}

        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        left, right = 0, 0
        valid = 0
        res = []

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                if c in wind:
                    wind[c] += 1
                else:
                    wind[c] = 1
                if wind[c] == need[c]:
                    valid += 1

            # 提前收缩窗口,保证窗口中全为想要的字符串
            while right - left >= len(t):
                if valid == len(need.keys()):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    #print(f"wind:{wind}, need:{need}")
                    if wind[d] == need[d]:
                        valid -= 1
                    wind[d] -= 1
        return res
