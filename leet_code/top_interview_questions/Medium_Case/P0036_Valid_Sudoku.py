class Solution:
    @staticmethod
    def isValidSudokuRow(grid) -> bool:
        for lst in grid:
            data = [i for i in lst if i != '.']
            # check duplicate
            if len(data) != len(set(data)):
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        if not self.isValidSudokuRow(board):
            return False
        # check column
        if not self.isValidSudokuRow(zip(*board)):
            return False
        
        # get block 3*3
        block = [[] for i in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                block[(i//3)*3+j//3].append(board[i][j])
        
        print(block)
        # check block 3*3
        if not self.isValidSudokuRow(block):
            return False
        
        return True
