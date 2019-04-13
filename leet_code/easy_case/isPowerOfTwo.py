class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print("Here!")
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            while n > 1:
                if n % 2 == 0:
                    n = n / 2
                else:
                    return False
                if n == 1:
                    return True


# if __name__ == '__main__':
a = Solution()
a.isPowerOfTwo(1124)
