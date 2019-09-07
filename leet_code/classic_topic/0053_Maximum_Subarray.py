class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # modify nums inplace, turn nums[i] into sum of nums[k:i]
        for i in range(1,len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
