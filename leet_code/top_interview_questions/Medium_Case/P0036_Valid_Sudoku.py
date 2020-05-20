class Solution:
    @staticmethod
    def isValidSudokuRow(grid) -> bool:
        for lst in grid:
            data = [i for i in lst if i != "."]
            # check duplicate
            if len(data) != len(set(data)):
                return False
        return True

    def isValidSudoku(self, board]) -> bool:
        # check row
        if not self.isValidSudokuRow(board):
            return False
        # check column
        if not self.isValidSudokuRow(zip(*board)):
            return False

        # get block 3*3
        block = [[] for i in range(9)]
        for k in range(0, 3):
            # i=1 指上面三个
            for i in range(0 + 3 * k, 3 + 3 * k):
                for j in range(0, 3):
                    # the first block
                    block[3 * k + 0].append(board[i][j])
                for j in range(3, 6):
                    # the second block
                    block[3 * k + 1].append(board[i][j])
                for j in range(6, 9):
                    # the third block
                    block[3 * k + 2].append(board[i][j])
        # print(block)
        # check block 3*3
        if not self.isValidSudokuRow(block):
            return False

        return True
