"""
76. Minimum Window Substring
Hard

Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:

Input: s = "a", t = "a"
Output: "a"
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        # t会不会有重复的字符串? 可能会
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        left, right = 0, 0
        # valid 表示满足条件的字符个数
        valid = 0

        # 记录结果
        start = 0
        length = float("inf")

        while right < len(s):
            c = s[right]
            # 右移
            right += 1

            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1

                # 字符相同且数量一样就加一
                if need[c] == window[c]:
                    valid += 1

            # 保证字符数的情况下左移窗口
            while valid == len(need.keys()):
                # print(f"window:{window}")
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                # 移动窗口左边
                left += 1
                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1

        return s[start : start + length] if length != float("inf") else ""
