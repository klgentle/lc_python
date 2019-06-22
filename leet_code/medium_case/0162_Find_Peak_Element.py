class Solution:
    def findPeakElement(self, nums: list) -> int:
        # TODO logarithmic complexity.
        l = len(nums)
        if l == 1:
            return 0
        elif l == 2:
            return 0 if nums[0] > nums[1] else 1
        elif l == 0:
            return None
        else:
            if nums[0] > nums[1]:
                return 0
            elif nums[l-2] < nums[l-1]:
                return l-1
            
        for i in range(1,l-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
