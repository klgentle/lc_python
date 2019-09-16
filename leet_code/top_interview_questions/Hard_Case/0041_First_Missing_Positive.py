from pysnooper import snoop


class Solution:
    #@snoop()
    def firstMissingPositive(self, nums: list) -> int:
        if 1 not in nums:
            return 1
        l = len(nums)
        max_num = max(nums)
        min_num = min(nums)
        if min_num < 0:
            min_num = 1
        
        # if missing one find it
        for i in range(min_num+1, max_num+2):
            #print(f"test i:{i}")
            if i not in nums:
                return i

if __name__ == "__main__":
    a = Solution()
    nums = [1,3,3] 
    b = a.firstMissingPositive(nums)
    print(b)
