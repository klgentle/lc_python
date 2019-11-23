class Solution:
    def myPow(self, x: float, n: int) -> float:
        out = 1
        flag = '+'
        if n < 0:
            flag = '-'
            n = abs(n)
        while n > 0:
            out *= x
            n -= 1
        return out if flag =='+' else 1/out
