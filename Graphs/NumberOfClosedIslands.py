#---------------Problem: 1254---------------

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0

        def dfs(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS:
                return 0
            if grid[r][c] or (r,c) in visit:
                return 1
            visit.add((r,c))
            return min(dfs(r+1,c), dfs(r-1,c), dfs(r,c+1), dfs(r, c-1))

        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c] and (r,c) not in visit:
                    res += dfs(r,c)

        return res