class Solution:
    def divisorGame(self, N: int) -> bool:
        # 可以用归纳法证明，当N为偶数时，Alice会win
        """
        N == 2 Alice (Choosing) win;
        假设 N == M (偶数) 时 Alice (Choosing) win, 则 M+2 时 Alice 也会 win
        当 N = m+1 时, Alice会输，因为奇数只能被奇数整除，所以alice取完数后，剩下偶数，所以对方(Choosing)会赢。
        当 n = m+2 (偶数) 时，Alice 先取1，上面已经证明当N=m+1时Choosing 的人会输，所以n = m+2 (偶数) 时，Alice会赢。
        """
        return N % 2 == 0
