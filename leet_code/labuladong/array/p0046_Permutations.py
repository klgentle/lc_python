"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrace(nums, trace=[], result=[]):
            if not nums:
                # reason why we are copying here is because at "lists are passed by reference" and since we are maintaining only one path
                #result.append(trace[::])
                result.append(trace.copy()) # 需要复制trace, list.copy() 等价于 [::]

            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                trace.append(nums[i])
                backtrace(newNums, trace, result)
                trace.pop()
            return result

        return backtrace(nums)
