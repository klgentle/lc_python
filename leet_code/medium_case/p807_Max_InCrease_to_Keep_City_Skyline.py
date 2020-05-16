class Solution:
    @staticmethod
    def changeGridToColumn(grid: List[List[int]]) -> List[List[int]]:
        colList = []
        # colList初始化
        for i in range(len(grid[0])):
            colList.append([])
        
        for i, row in enumerate(grid):
            for j in range(len(row)):
                colList[j].append(row[j])
        #print(colList)
        return colList
    
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        修改后的 g[ij] = min(行最大值 max(g[i][]), 列最大值max(g[][j])) 
        """
        rowMax = []
        for row in grid:
            rowMax.append(max(row))
        #print(rowMax)
        
        colMax = []
        for col in self.changeGridToColumn(grid):
            colMax.append(max(col))
        #print(colMax)
        
        sum_increas = 0
        for i, row in enumerate(grid):
            for j, height in enumerate(row):
                sum_increas += min(rowMax[i], colMax[j]) - height
                
        return sum_increas
