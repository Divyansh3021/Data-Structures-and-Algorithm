#--------------Problem: 695--------------


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0

        def countArea(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            return (1 + countArea(i+1,j) + countArea(i-1,j) + countArea(i,j+1) + countArea(i,j-1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    maxArea = max(maxArea,countArea(i,j))
        
        return maxArea

#T.C. = O(m.n)