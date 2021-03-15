"""
494. Target Sum
Medium

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.target = S
        self.nums = nums
        self.memo = {}
        return self.dp(len(nums)-1, 0)


    def dp(self, index, curr_sum):
        # Optimize
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        # base case
        if index < 0 and curr_sum == self.target:
            return 1
        if index < 0:
            return 0

        # decision
        positive = self.dp(index-1, curr_sum + self.nums[index])
        negetive = self.dp(index-1, curr_sum - self.nums[index])

        self.memo[(index, curr_sum)] = positive + negetive
        return self.memo[(index, curr_sum)]
