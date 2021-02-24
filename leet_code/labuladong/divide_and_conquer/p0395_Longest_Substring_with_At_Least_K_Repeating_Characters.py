"""
395. Longest Substring with At Least K Repeating Characters
Medium

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        if len(s) < k:
            return 0

        counter = Counter(s)
        #print(f"counter:{counter}")
        for p, v in enumerate(s):
            if counter[v] < k:
                # jump over p
                return max(self.longestSubstring(s[:p],k), self.longestSubstring(s[p+1:],k))

        return len(s)
