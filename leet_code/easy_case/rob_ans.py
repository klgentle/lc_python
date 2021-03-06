# coding:utf8
import pysnooper


class Solution(object):
    # debug here
    # @pysnooper.snoop('/home/kl/log/leet_code/1.log')
    @pysnooper.snoop()
    def rob(self, nums: list) -> int:
        """
        :type nums: List[int]
        """
        last = 0
        now = 0
        for i in nums:
            # 这是一个动态规划问题
            last, now = now, max(last + i, now)
        return now


if __name__ == "__main__":
    a = Solution()
    lst1 = [1, 2, 3, 1]
    lst2 = [2, 1, 1, 2]
    a.rob(lst1)
    # a.rob(lst2)
