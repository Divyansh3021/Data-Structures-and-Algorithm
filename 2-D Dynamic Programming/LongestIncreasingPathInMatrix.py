#--------------Problem: 329----------------

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(matrix), len(matrix[0])

        def helper(r,c, prevVal):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal):
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            dp[(r,c)] = max(
                res,
                1 + helper(r+1, c, matrix[r][c]),
                1 + helper(r-1, c, matrix[r][c]), 
                1 + helper(r, c+1, matrix[r][c]), 
                1 + helper(r, c-1, matrix[r][c])
            )
            return dp[(r,c)]
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in dp:
                    helper(i,j, float("-inf"))

        return max(dp.values())