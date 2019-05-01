class Solution:
    """
    53. 最大子序和
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    """

    def maxSubArray(self, nums: list) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(0, nums[i - 1])
        return max(nums)
