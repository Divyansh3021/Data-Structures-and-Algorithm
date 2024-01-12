#-----------------Problem: 115--------------------

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        dp = {}

        def helper(i, j): #s->i t->j
            if i >= len(s) or j >= len(t):
                if j >= len(t):
                    return 1
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if s[i] == t[j]:
                dp[(i,j)] = helper(i+1, j+1) + helper(i+1, j)
            else:
                dp[(i,j)] = helper(i+1, j)
            
            return dp[(i,j)]
        
        return helper(0,0)