# import pysnooper


class Solution:
    """
    双指针 Double pointer
    """
    #@pysnooper.snoop()
    def maxArea(self, height: "list[int]") -> int:
        res = 0
        l = 0
        r = len(height) - 1
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                # KEEP THE MAX HEIGHT
                l += 1
            else:
                r -= 1

        print(res)
        return res


if __name__ == "__main__":
    a = Solution()
    a.maxArea([1, 2, 1])
