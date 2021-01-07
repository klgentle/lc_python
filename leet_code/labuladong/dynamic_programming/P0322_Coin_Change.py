"""
322. Coin Change TODO enhance
Medium

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

"""


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # coins:List[int]
        res = {}
        res[0] = 0

        def dp(n):
            # dp(n) = min(dp(n-coin)+1, dp(n))
            if n in res.keys():
                return res[n]
            if n < 0:
                return -1
            res[n] = float("INF")
            for coin in coins:
                if dp(n - coin) == -1:
                    continue
                res[n] = min(dp(n - coin) + 1, res[n])

            return res[n] if res[n] != float("INF") else -1

        return dp(amount)
