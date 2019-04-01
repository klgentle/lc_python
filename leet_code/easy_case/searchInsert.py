class Solution:
    def searchInsert(self, nums, target):
        """
        type: List[int]
        rtype:int
        """
        if target in nums:
            return nums.index(target)
        else:
            return self.searchPosition(nums, target)

    def searchPosition(self, nums, target):
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        for i in range(0,len(nums)-1):
            if nums[i] < target and target < nums[i+1]:
                return i+1
