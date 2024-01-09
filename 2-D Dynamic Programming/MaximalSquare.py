#------------------Problem: 221---------------------

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix),  len(matrix[0])
        dp = {}
        def helper(r,c):
            if r >= ROWS or c >= COLS:
                return 0

            if (r,c) not in dp:
                down = helper(r+1,c)
                right = helper(r,c+1)
                diag = helper(r+1,c+1)
                dp[(r,c)] = 0
                if matrix[r][c] == "1":
                    dp[(r,c)] = 1 + min(down, right, diag)

            return dp[(r,c)]

        helper(0,0)

        return max(dp.values())**2