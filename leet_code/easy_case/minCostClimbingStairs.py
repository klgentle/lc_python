class Solution:
    # leetcode 746. 使用最小花费爬楼梯
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) # add zero to jump to top
        c = []
        c.append(cost[0]) # c[0], c[1]
        c.append(cost[1])
        l = len(cost)
        for i in range(2,l):
            c.append(min(c[i-2] + cost[i], c[i-1]+ cost[i]))
            
        print(f"c: {c}")
        print(f"min cost: {c[-1]}")
        return c[-1]
