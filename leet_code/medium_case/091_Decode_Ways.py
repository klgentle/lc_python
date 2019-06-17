from pysnooper import snoop
class Solution:
    """
    s = '226'
    set[0] = 2
    set[1] = [[2,2],[22]]
    set[2] = [[2,26],[22,6],[2,2,6]]
    """

    @snoop()
    def numDecodings(self, s: str) -> int:
        if not s or s.startswith('0'): return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if s[i - 1] != '0' and int(s[i - 1:i + 1]) <= 26:
                tmp = dp[i - 2] if i - 2 >= 0 else 1
                dp[i] += tmp
        return dp[-1]

# todo return multiply of len of all subset
if __name__ == "__main__":
    a = Solution()
    s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
    a.numDecodings(s)
