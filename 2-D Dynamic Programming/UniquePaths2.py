#---------------------Problem: 63-----------------------

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [0] * COLS
        dp[COLS - 1] = 1
        for i in range(ROWS -1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if grid[i][j]:
                    dp[j] = 0
                elif j + 1 < COLS:
                    dp[j] = dp[j] + dp[j+1]
        return dp[0]