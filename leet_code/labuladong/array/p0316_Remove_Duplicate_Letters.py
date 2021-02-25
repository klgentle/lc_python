"""
316. Remove Duplicate Letters
Medium

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        去重，最简单的是建立清单，如果不在清单中就加入，在就跳过；
        如果要保证 lexicographical order，可以在加入时，弹出之前加入的元素（条件是弹出的元素，后面还可以加入）。
        """
        count = Counter(s)
        stack = []

        for c in s:
            count[c] -= 1
            if c not in stack:
                while stack and c < stack[-1] and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)

        return "".join(stack)
