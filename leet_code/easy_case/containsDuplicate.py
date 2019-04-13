class Solution:
    def containsDuplicate(self, nums):
        l_set = len(set(nums))
        l_nums = len(nums)
        """        
        if l_nums > l_set:
            return True
        else:
            return False
        """
        return True if l_nums > l_set else False
