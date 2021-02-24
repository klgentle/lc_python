"""
567. Permutation in String
Medium

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""

class Solution:
    def checkInclusion(self, t: str, s: str) -> bool:
        """
        套用滑动窗口的框架，提前收缩窗口，这样可以保证进来的是目标字符的排列
        """
        if t in s or t[::-1] in s:
            return True

        need = {}
        wind = {}

        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        left, right = 0, 0
        valid = 0

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
                    return True
                d = s[left]
                left += 1
                if d in need:
                    if wind[d] == need[d]:
                        valid -= 1
                    wind[d] -= 1

        return False
