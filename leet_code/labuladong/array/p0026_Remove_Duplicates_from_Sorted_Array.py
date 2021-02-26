"""
26. Remove Duplicates from Sorted Array
Easy

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            while nums[fast] != nums[slow]:
                slow += 1
                #维护 nums[0..slow] 无重复
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1
