#----------------Problem: 64--------------------

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = [[float("inf")] * (COLS + 1) for i in range(ROWS+1)]
        res[ROWS][COLS-1] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS-1, -1,-1):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
        return res[0][0]