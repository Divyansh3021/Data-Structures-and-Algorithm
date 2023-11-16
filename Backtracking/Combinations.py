#------Problem:77------
#------T.C. k*n^k-------

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        subList = []
        def dfs(initial, final, subList):
            if len(subList) == k:
                res.append(subList.copy())
                return
            
            if initial <= final:
                subList.append(initial)
                dfs(initial + 1, final, subList)

                subList.pop()
                dfs(initial + 1, final, subList)

        dfs(1, n, subList)
        return res