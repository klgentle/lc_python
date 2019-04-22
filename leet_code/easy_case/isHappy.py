class Solution:
    def isHappy(self, n: int) -> bool:
        m = 0
        return False if self.squareSum(n,m) != 1 else True
    
    def squareSum(self, n: int, m:int) -> int:    
        m += 1
        s = str(n)
        sum = 0
        if m > 9:
            return -1
        if len(s) > 1:
            for i in s:
                sum += int(i) ** 2
        else:
            sum += n ** 2
        #print(f"sum:{sum}")
        return 1 if sum == 1 else self.squareSum(sum,m)


if __name__ == '__main__':
    a = Solution()
    a.isHappy(2)
