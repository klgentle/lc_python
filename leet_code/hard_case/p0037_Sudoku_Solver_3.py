import heapq

class Solution:
    #Does a DFS
    def solve(self, board, heap):
        if len(heap)==0:
            return True
        # (len(remaining), idy, idx, remaining)
        procitem = heapq.heappop(heap)
        if procitem[0] == 0:
            return False
        for value in procitem[3]:
            board[procitem[1]][procitem[2]] = value
            newheap = []
            for size, idy, idx, remaining in heap:
                matchedrow = procitem[1]==idy
                matchedcol = procitem[2]==idx
                matchedbox = (procitem[1]//3*3+procitem[2]//3)==(idy//3*3+idx//3)
                if (matchedrow or matchedcol or matchedbox) and value in remaining:
                    heapq.heappush(newheap,(size-1,idy, idx, remaining - {value}))
                else:
                    heapq.heappush(newheap, (size, idy, idx, remaining))
            if self.solve(board, newheap):
                return True
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        allnums = {'1','2','3','4','5','6','7','8','9'}
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        rowtodo = {}
        coltodo = {}
        todo = set()
        for idy, row in enumerate(board):
            for idx, val in enumerate(row):
                if val == '.':
                    todo.add((idy,idx))
                else:
                    rows[idy].add(val)
                    cols[idx].add(val)
                    idbox = idy//3*3+idx//3
                    boxes[idbox].add(val)
        heap = []
        
        for (idy, idx) in todo:
            row = rows[idy]
            col = cols[idx]
            box = boxes[idy//3*3+idx//3]
            remaining = allnums - row - col - box
            heapq.heappush(heap, (len(remaining), idy, idx, remaining))

        self.solve(board, heap)
