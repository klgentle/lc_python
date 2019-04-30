class NumArray:

    def __init__(self, nums: list):
        self.sum = [0]
        s = 0
        for n in nums:
            s += n
            self.sum.append(s)
        

    def sumRange(self, i: int, j: int) -> int:
        
        print(f"i:{i}")
        print(f"sum[i]:{self.sum[i]}")
        print(f"j:{j}")
        print(f"sum[j]:{self.sum[j]}")
        return self.sum[j+1] - self.sum[i]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    a = NumArray(nums)
    a.sumRange(3,5)
