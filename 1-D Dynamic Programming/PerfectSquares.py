#---------------Problem: 279------------------

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0

        for target in range(1, n+1):
            for s in range(target):
                square = s * s
                if square > target:
                    break
                dp[target] = min(dp[target], dp[target-square] + 1)
        return dp[target]