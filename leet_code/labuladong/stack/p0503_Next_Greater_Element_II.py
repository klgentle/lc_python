"""
503. Next Greater Element II
Medium

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000. 
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        # 假设已经构造出两倍的nums
        for i in range(2 * n - 2, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if stack:
                res[i % n] = stack[-1]

            stack.append(nums[i % n])

        return res
