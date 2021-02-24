"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}

        valid = 0
        left, right = 0, 0
        max_valid = 0

        while right < len(s):
            c = s[right]
            right += 1

            if c not in window:
                valid += 1
                max_valid = max(max_valid, valid)
                window[c] = 1
            else:
                window[c] += 1

            while window[c] > 1:
                d = s[left]
                #print(f"right:{right}, left:{left}, d:{d}")
                left += 1

                if window[d] == 1:
                    valid -= 1
                    # del 字典中删除key 
                    del window[d]
                else:
                    window[d] -= 1

        return max_valid
