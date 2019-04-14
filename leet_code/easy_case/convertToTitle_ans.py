class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""
        while n > 0:
            n -= 1
            ans += chr(n % 26 + ord("A"))
            n //= 26
        print(ans[::-1])
        return ans[::-1]


if __name__ == "__main__":
    a = Solution()
    a.convertToTitle(52)
