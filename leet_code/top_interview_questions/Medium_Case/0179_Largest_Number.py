class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # improve step by step
        if set(nums) == {0}:
            return "0"
        nums_str = [str(i) for i in nums]
        ret_len = len("".join(nums_str))
        
        nums_str_ind = [[str(i),ind] for ind, i in enumerate(nums)]
        # '0', 'x' pad is not perfect, use the last digit to test, use the data it's self to test
        l = len(nums)
        #nums_test = [[d[0].ljust(ret_len,d[0]), d[1]] for d in nums_str_ind]
        # cope l times and return ret_len
        nums_test = [[(d[0]*l)[:ret_len], d[1]] for d in nums_str_ind]
        nums_order_desc = sorted(nums_test, key = lambda d: d[0], reverse=True)
        #print(f"nums_order_desc:{nums_order_desc}")
        ret = ""
        for d in nums_order_desc:
            ret += str(nums[d[1]])
        return ret
