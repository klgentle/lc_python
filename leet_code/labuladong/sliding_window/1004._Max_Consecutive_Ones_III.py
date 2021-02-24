"""
1004. Max Consecutive Ones III
Medium

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
"""

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, 0
        windFreq = defaultdict(int)
        maxFreq = 0
        maxLen = 0

        while right < len(A):
            a = A[right]
            right += 1
            windFreq[a] += 1

            # 与第424题唯一的不同在于此处的 if, 只有取1时，才计算 maxFreq
            if a == 1:
                maxFreq = max(maxFreq, windFreq[a])

            if (right - left) - maxFreq > K:
                windFreq[A[left]] -= 1
                left += 1
            else:
                maxLen = max(maxLen, right - left)

        return maxLen
