"""
80. Remove Duplicates from Sorted Array II
Medium

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
"""

from collections import Counter


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        # delete from then end
        for v in nums[::-1]:
            #print(f"v:{v}, count[v]:{count[v]}")
            if count[v] > 2:
                nums.remove(v)
                count[v] -= 1

        return len(nums)
