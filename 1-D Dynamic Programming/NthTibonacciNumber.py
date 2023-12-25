#--------------------Problem: 1137---------------------

class Solution:
    def tribonacci(self, n: int) -> int:
        F = []
        F.append(0)
        F.append(1)
        F.append(1)
        for i in range(3,n+1):
            ele = F[i-1] + F[i-2] + F[i-3]
            F.append(ele)
        
        return F[n]