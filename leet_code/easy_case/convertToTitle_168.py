# leetcode 168

class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = ''
        while n > 0 :
            n -= 1 # why ?
            print(f"n:{n}")
            ret = chr(n % 26 + ord("A")) + ret
            print(f"ret:{ret}")
            n //= 26
        print(f"ret: {ret}")
        return ret


if __name__ == "__main__":
    a = Solution()
    a.convertToTitle(52)
    # print("next------------------\n")
    # a.convertToTitle(701)
    # print("next------------------\n")
    # a.convertToTitle(27)
