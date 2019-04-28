class Solution:
    def missingNumber(self, nums: list) -> int:
        l = len(nums)
        lst = [i for i in range(0,l+1)]
        for i in set(lst) - set(nums):
            return i

if __name__ == '__main__':
    a = Solution()
    #a.missingNumber([3,0,1])
    a.missingNumber([0])
