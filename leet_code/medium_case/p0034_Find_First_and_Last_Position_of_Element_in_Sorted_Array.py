class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        return [nums.index(target), self.searchEnding(nums, target)]
    
    def searchEnding(self, nums: List[int], target: int) -> int:
        ind = nums.index(target)
        for num in nums[nums.index(target)+1:]:
            if num == target:
                ind += 1
            else:
                break
        return ind
