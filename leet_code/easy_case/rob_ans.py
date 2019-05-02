class Solution(object):
    def rob(self, nums:list):-> int
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0 
        now = 0
        for i in nums: 
            #这是一个动态规划问题
            last, now = now, max(last + i, now)
        return now
