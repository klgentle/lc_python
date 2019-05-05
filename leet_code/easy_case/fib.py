class Solution:
    def fib(self, N:int)->int:
        F = [0, 1]
        while len(F) <= N:
            F.append(F[-1] + F[-2])
        return F[N]
