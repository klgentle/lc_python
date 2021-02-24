"""
424. Longest Repeating Character Replacement
Medium

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windFreq = defaultdict(int)
        start, end = 0, 0
        maxWindFreq, maxLen = 0, 0
        
        while end < len(s):
            c = s[end]            
            
            windFreq[c] += 1
            maxWindFreq = max(maxWindFreq, windFreq[c])
            
            # 比较区间长度跟区间最大词频的差异
            if (end - start + 1) - maxWindFreq > k:
                windFreq[s[start]] -= 1
                start += 1
            else:
                maxLen = max(maxLen, end - start + 1)
            
            end += 1
            
        return maxLen
