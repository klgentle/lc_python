class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
       
        for i in (2,3,5):
            while num % i == 0:
                num //= i
        #print(True if num == 1 else False)
        return True if num == 1 else False


if __name__ == '__main__':
    a = Solution()
    a.isUgly(937351770)
