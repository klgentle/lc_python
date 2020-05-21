from collections import defaultdict
from collections import deque


class Solution:
    def solveSudoku(self, board) -> None:
        rows, cols, blocks, toVisits = defaultdict(set), defaultdict(set), defaultdict(set), deque()
        values = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    t = (r//3, c//3)
                    blocks[t].add(board[r][c])
                else:
                    toVisits.append((r, c))
        
        def dfs():
            if not toVisits:
                return True
            
            r, c = toVisits[0]
            t = (r//3, c//3)
            for v in values - rows[r] - cols[c] - blocks[t]:
                toVisits.popleft()
                board[r][c] = v
                rows[r].add(v)
                cols[c].add(v)
                blocks[t].add(v)

                if dfs():
                    return True
                else:
                    toVisits.appendleft((r, c))
                    board[r][c] = "."
                    rows[r].discard(v)
                    cols[c].discard(v)
                    blocks[t].discard(v)
                    
            return False
        dfs()
