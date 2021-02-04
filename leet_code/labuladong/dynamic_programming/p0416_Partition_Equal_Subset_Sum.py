"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 子背包问题

        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False

        sub_sum = int(nums_sum / 2)

        dp = [False] * (sub_sum + 1)
        dp[0] = True

        for i in range(len(nums)):
            # 不需要对dp[0]赋值
            for j in range(sub_sum,0,-1):
                if j >= nums[i-1]:
                    dp[j] = dp[j] or dp[j - nums[i-1]]

        #print(f"{dp}")
        return dp[sub_sum]
