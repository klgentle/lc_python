class Solution:
    def removeAll(self, nums, a):
        times = nums.count(a)
        while times > 1:
            nums.remove(a)
            times -= 1

    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 1:
            a = nums[i]
            if nums[i] == nums[i + 1]:
                # print('i==j,i:{},j:{}'.format(i,i+1))
                # nums.remove(a)
                self.removeAll(nums, a)
            i += 1
        l = len(nums)
        print(l)
        return l
