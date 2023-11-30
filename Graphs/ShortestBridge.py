#--------------Problem: 934--------------

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[1,0], [-1,0], [0,1],[0, -1]]

        def IsValid(r, c):
            return r < 0 or c < 0 or r == N or c == N

        visit = set()
        def dfs(r,c):
            if IsValid(r,c) or not grid[r][c] or (r,c) in visit:
                return
            visit.add((r,c))
            for direc in directions:
                dr, dc = direc
                dfs(r + dr, c + dc)

        def bfs():
            q = deque(visit)
            res = 0

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if IsValid(row, col) or (row, col) in visit:
                            continue
                        if grid[row][col]:
                            return res
                        q.append([row,col])
                        visit.add((row,col))
                res += 1
        
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()