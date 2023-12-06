#---------------Problem : 1020---------------

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
                
        visit = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or not grid[r][c]:
                return 0

            visit.add((r,c))
            res = 1
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            for dr, dc in directions:
                res += dfs(r+dr, c+dc)
            return res

        totalLand = 0
        borderLand = 0
        for r in range(ROWS):
            for c in range(COLS):
                totalLand += grid[r][c]

                if ((r in [0, ROWS-1] or c in [0, COLS-1]) and grid[r][c] and (r,c) not in visit):
                    borderLand += dfs(r,c)
        return totalLand - borderLand