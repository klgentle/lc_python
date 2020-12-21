"""
78.Subsets

Given an integer array nums, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

"""


class Solution:
    # 利用 list + 运算实现元素的组合
    # +类似于list的extend运算
    def subsets(self, nums) -> list:
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res
