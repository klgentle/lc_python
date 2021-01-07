class Solution:
    # 动态规划，bottom up会比直接迭代快
    def coinChange(self, coins: List[int], amount: int) -> int:
        # step1 初始化
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        # step2 状态转移
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        # step3 结果返回
        return dp[amount] if dp[amount] != float("inf") else -1
