#-----------Problem: 474-----------

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}  #(i,m,n) -> no. of strings in subset

        def helper(i, m, n):
            if i == len(strs):
                return 0

            if (i,m,n) in dp:
                return dp[(i,m,n)]
            
            zeroes, ones = strs[i].count("0"), strs[i].count("1")
            dp[(i,m,n)] = helper(i+1,m,n)

            if zeroes <= m and ones <= n:
                dp[(i,m,n)] = max(dp[(i,m,n)], 1 + helper(i+1, m - zeroes, n - ones))
            
            return dp[(i,m,n)]
        
        return helper(0,m,n)