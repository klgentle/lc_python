#!/usr/bin/env python3
# coding:utf8

import pysnooper
import pdb


class Solution:
    """
    # 198
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, the only constraint 
    stopping you from robbing each of them is that adjacent houses 
    have security system connected and it will automatically contact the 
    police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money 
    of each house, determine the maximum amount of money you can rob tonight 
    without alerting the police.
    """

    # @pysnooper.snoop()
    def rob(self, nums: list) -> int:
        print(f"nums:{nums}")
        s = max(nums)
        ind = nums.index(s)
        l = len(nums)

        add_ind = ind
        for i in range(ind - 2, -1, -2):
            if i - 1 >= 0:
                if nums[i] >= nums[i - 1] and abs(i - add_ind) > 1:
                    s += nums[i]
                    add_ind = i
                else:
                    s += nums[i - 1]
                    add_ind = i - 1

        # number after ind
        for i in range(ind + 2, l, 2):

            if i + 1 < l:
                print(f"i+1:{i+1}")
                if nums[i] >= nums[i + 1] and i - add_ind > 1:
                    s += nums[i]
                    add_ind = i
                else:
                    s += nums[i + 1]
                    add_ind = i + 1

        print(f"s:{s}")
        return s


if __name__ == "__main__":
    a = Solution()
    lst1 = [1, 2, 3, 1]
    lst2 = [2, 1, 1, 2]
    # a.rob(lst1)
    try:
       _ = a.rob(lst2)
    except (Exception, e):
        pdb.set_trace()
