"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:
                return

            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        # pass the duplicate
                        # if nums[l] is the same with nums[l-1], then no need to consider nums[l]
                        while (l < r and nums[l] == nums[l - 1]):  
                            l += 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1

            else:  # find recursive
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findSum(
                            nums[i + 1 :],
                            target - nums[i],
                            N - 1,
                            result + [nums[i]],
                            results,
                        )

        results = []
        findSum(sorted(nums), target, 4, [], results)
        return results
