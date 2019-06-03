from pysnooper import snoop

class Solution:
    @snoop()
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        results = []
        for index in range(len(nums)):
            for item in self.permute(nums[:index] + nums[index+1:]):
                results.append([nums[index]] + item)
        
        return results


if __name__ == '__main__':
    a = Solution()
    a.permute([1,2,3])
