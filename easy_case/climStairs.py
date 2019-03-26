import math

class Solution:
    def climbStairs(self, n: int) -> int:
        print('n:', n)
        ret = 0
        for i in range(0,n+1):
            for j in range(0,n+1):
                if i + 2*j != n:
                    continue
                print('i:{0},j:{1}'.format(i,j))
                y = 0
                if i== 0 or j ==0:
                    y = 1
                else:
                    y = math.factorial(i+j)/(math.factorial(j)*math.factorial(i))
                ret += int(y)
                print('y:', y)
        print('ret:', ret)
        return ret

if __name__ == '__main__':
    a = Solution()
    a.climbStairs(4)
