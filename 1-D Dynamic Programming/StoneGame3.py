#---------------------Problem: 1406----------------------

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}

        def helper(i):
            if i == len(stoneValue):
                return 0
            if i in dp:
                return dp[i]
            
            res = float("-inf")
            for j in range(i, min(i+3, len(stoneValue))):
                res = max(res, sum(stoneValue[i:j+1]) - helper(j+1))
            dp[i] = res
            return res
        
        res = helper(0)
        if res > 0:
            return "Alice"
        elif res == 0:
            return "Tie"
        else:
            return "Bob"