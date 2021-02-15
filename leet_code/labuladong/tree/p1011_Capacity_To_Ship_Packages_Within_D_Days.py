"""
1011. Capacity To Ship Packages Within D Days
Medium

A conveyor belt has packages that must be shipped from one port to another within D days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
"""


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        maxCapa = sum(weights)

        # 用二分法进行优化
        left = max(weights)
        while left < maxCapa:
            c_mid = int((left + maxCapa) / 2)
            if self.canShip(weights, D, c_mid):
                maxCapa = c_mid
            else:
                left = c_mid + 1
        return left

    def canShip(self, w, D, c):
        """
        此函数思想挺好，每天重新分配容量，最终看w[i]是否分配完。
        """
        i = 0
        # 注意取值的边界条件
        for day in range(D):
            maxC = c
            while maxC - w[i] >= 0:
                maxC -= w[i]
                i += 1
                if i == len(w):
                    return True
