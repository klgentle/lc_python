class Solution:
    """
    执行用时: 1624 ms, 在Number of Boomerangs的Python3提交中击败了79.56% 的用户
    """

    def numberOfBoomerangs(self, points):
        """
        降维
        看似三个点之间比较，其实只要比两个点
        计算其他点到当前点的距离，如果相同距离的点有2个以上则满足(有An2种可能)
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        sum1 = 0
        for i in range(n):
            dic = {}
            for j in range(n):
                # 排除这个点本身
                if j != i:
                    dis = self.distance(points[i], points[j])
                    if dis not in dic:
                        dic[dis] = 1
                    else:
                        dic[dis] += 1
            # print(dic)
            for value in dic.values():
                if value >= 2:
                    sum1 += int(value * (value - 1))
        return sum1

    def distance(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
