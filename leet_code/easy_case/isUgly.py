import math
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        fact_all = set((2, 3, 5))
        fact_num = self.getNumFactors(num)
        print(f"fact_num:{fact_num}")
        # 判断集合 y 的所有元素是否都包含在集合 x 中：x.issuperset(y)
        print(f"fact_all.issuperset(fact_num):{fact_all.issuperset(fact_num)}")
        return fact_all.issuperset(fact_num)

    def getNumFactors(self, num):
        factor = set()
        tmp = 2
        while tmp < int(math.sqrt(1 + num)) + 1:
            k = num % tmp
            if k == 0:
                factor.add(tmp)
                num = num / tmp  # 更新
            else:
                tmp = tmp + 1  # 同时更新除数值，不必每次都从头开始
        return factor


if __name__ == '__main__':
    a = Solution()
    a.isUgly(14)
