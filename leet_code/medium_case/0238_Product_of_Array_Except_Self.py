class Solution:
    """
    List set value is faster than append value
    """
    def productExceptSelf(self, nums: list) -> list:
        length = len(nums)
        left = [1]*length
        right = [1]*length
        ret = [1]*length
        for i in range(1,length):
            left[i] = left[i-1] * nums[i-1]

        for i in range(length-1, 0, -1):
            right[i-1] = right[i]*nums[i]

        for i in range(length):
            ret[i] = left[i]*right[i]

        return ret
