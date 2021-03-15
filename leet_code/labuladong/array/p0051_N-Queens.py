"""
51. N-Queens
Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(0, n)]
        self.backtrace(board, 0)
        return self.res

    def backtrace(self, board, row):
        if row == len(board):
            board2 = ["".join(row) for row in board]
            self.res.append(board2)
            return

        n = len(board[row])
        for col in range(n):
            if not self.isValid(board, row, col):
                continue

            # make choice
            board[row][col] = "Q"
            # move
            self.backtrace(board, row + 1)
            # backtrace
            board[row][col] = "."

    def isValid(self, board, row, col):
        n = len(board)
        # 决断列是否冲突
        for r in range(n):
            if board[r][col] == "Q":
                return False

        # 决断左上方是否冲突
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # 决断右上方是否冲突
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True
