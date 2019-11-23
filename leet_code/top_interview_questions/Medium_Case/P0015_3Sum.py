class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Double pointers can reduce the number of for loops
        nums = sorted(nums)
        sum_of_zero = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    sum_of_zero.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l]==nums[l+1]:
                        l += 1
                    while l < r and nums[r]==nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1            

        return sum_of_zero
