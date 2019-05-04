# coding:utf8
import pysnooper


class Solution:
    # @pysnooper.snoop()
    def validPalindrome(self, s: str) -> bool:
        r = s[::-1]
        if r == s:
            return True
        l = len(s)
        for i in range(l):
            if s[i] != r[i]:
                m = s[:i] + s[i + 1 :]
                n = r[:i] + r[i + 1 :]
                return m == m[::-1] or n == n[::-1]


if __name__ == "__main__":
    a = Solution()
    s = "cbbcc"
    a.validPalindrome(s)
