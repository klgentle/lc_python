# coding:utf8
#import pysnooper


class Solution(object):
    # debug here
    #@pysnooper.snoop()
    def rob(self, nums: list) -> int:
        """
        :type nums: List[int]
        # 这是一个动态规划问题
        """
        l = len(nums)
        opt = [0, 0]
        opt.extend([None] * (l - 2))
        if not nums:
            return 0
        if l == 1:
            return nums[0]
        opt[0], opt[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, l):
            opt[i] = max(opt[i - 1], opt[i - 2] + nums[i])
        return opt[-1]

if __name__ == "__main__":
    a = Solution()
    lst1 = [1, 2, 3, 1]
    lst2 = [2, 1, 1, 2]
    lst3 = [1, 1, 1, 2]
    # a.rob(lst1)
    a.rob(lst3)
