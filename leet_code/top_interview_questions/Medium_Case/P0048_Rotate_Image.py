import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        核心思想，行转列。
        此处有一个copy的坑，直接copy原二维数组，数据会变
        """
        original_matrix = copy.deepcopy(matrix)
        n = len(matrix)
        for c in range(n-1,-1,-1):
            old_row = n-1-c
            for r in range(n):
                #print(f"original_matrix[{old_row}][{r}]",original_matrix[old_row][r])
                matrix[r][c] = original_matrix[old_row][r]
           
        #print(matrix)
