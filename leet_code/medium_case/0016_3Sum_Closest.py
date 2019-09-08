"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
from pysnooper import snoop
class Solution:
    @snoop()
    def threeSumClosest(self, nums: list, target: int) -> int:
        total_list = []
        sum_closest = 0
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                total_list.append(total)
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return target
        print(f"total_list:{total_list}")
        distance = 90120908
        for total in total_list:
            if abs(total - target) <= distance:
                distance = abs(total - target)
                sum_closest = total
            
        return sum_closest


if __name__ == "__main__":
    lst = [6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10]
    target = -52
    a = Solution()
    a.threeSumClosest(lst, target)
    #print(sorted(lst))
