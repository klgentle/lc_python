class NumArray:

    def __init__(self, nums: list):
        self.sum = [0]
        s = 0
        for n in nums:
            s += n
            self.sum.append(s)
        

    def sumRange(self, i: int, j: int) -> int:
        
        return self.sum[j+1] - self.sum[i]
