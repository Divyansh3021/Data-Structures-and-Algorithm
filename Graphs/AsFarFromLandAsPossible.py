#-----------Problem: 1162-----------

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c]:
                    q.append([r,c])
        
        res = -1
        while q:
            r, c = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            res = grid[r][c]
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if min(newR, newC) >= 0 and max(newR, newC) < n and not grid[newR][newC]:
                    q.append([newR, newC])
                    grid[newR][newC] = grid[r][c] + 1
            
        return res - 1 if res > 1 else -1