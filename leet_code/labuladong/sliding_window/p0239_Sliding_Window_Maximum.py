"""
239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:

Input: nums = [9,11], k = 2
Output: [11]

Example 5:

Input: nums = [4,-2], k = 2
Output: [4]
"""
from collections import deque


class MonotonicQueue:
    """
    使用 deque 比直接使用 list 实现会高效一些
    """
    def __init__(self):
        self.q = deque()
        
    def push(self, n):
        # 删除所有小于n的元素
        while self.q and self.q[-1] < n:
            self.q.pop()
        self.q.append(n)
    
    def max(self):
        return self.q[0]
    
    def pop(self, n):
        if self.q[0] == n:
            self.q.popleft()

class MonotonicQueue0:
    def __init__(self):
        self.q = []

    def push(self, n):
        # 删除所有小于n的元素
        while self.q and self.q[-1] < n:
            self.q.pop()
        self.q.append(n)

    def max(self):
        return self.q[0]

    def pop(self, n):
        if self.q[0] == n:
            self.q.pop(0)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        res = []

        for i, v in enumerate(nums):
            if i < k - 1:
                window.push(v)
            else:
                window.push(v)
                res.append(window.max())
                window.pop(nums[i-k+1])

        return res


