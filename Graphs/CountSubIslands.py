#----------Problem: 1905----------
#----------T.C. = o(m.n)----------

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        count = 0

        def isIsland(i,j):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0 or (i,j) in visited:
                return True
            visited.add((i,j))
            res = True
            if grid1[i][j] == 0:
                res = False

            res = isIsland(i+1,j) and res
            res = isIsland(i-1,j) and res
            res = isIsland(i,j+1) and res
            res = isIsland(i,j-1) and res

            return res


        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]==1 and (i,j) not in visited and isIsland(i,j):
                    count += 1
        
        return count