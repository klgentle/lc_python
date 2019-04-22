class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_nums = max(nums)
        sum_nums = sum(nums)
        max_sum = max(max_nums, sum_nums)
        l = len(nums)
        print(f"max_sum:{max_sum}")

        if l == 1 or max_sum < 0:
            return max_sum
        m,n = 0,l
        max_list = nums
        for i,k in enumerate(nums):
            if k < 0:
                m += 1
            break

        print(f"max_sum:{max_sum}")
        return max_sum

if __name__ == '__main__':
    a = Solution()
    l = [-2, -1]
    a.maxSubArray(l)
