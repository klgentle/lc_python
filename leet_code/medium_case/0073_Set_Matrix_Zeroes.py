class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        step 1 find all zero position,
        step 2 set its entire row and column to 0 
        """
        # TODO A simple improvement uses O(m + n) space, but still not the best solution.  Could you devise a constant space solution?
        #zero_row = []
        zero_col = []
        for row, lst in enumerate(matrix):
            if 0 not in lst:
                continue
            for col, v in enumerate(lst):
                if v == 0:
                    #zero_row.append(row)
                    zero_col.append(col)
                    matrix[row] = [0] * len(lst)
            
            
        for ind, lst in enumerate(matrix):
            # set col to 0
            for col in zero_col:
                lst[col] = 0
