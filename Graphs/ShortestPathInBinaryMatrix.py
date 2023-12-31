#---------------Problem: 1091---------------

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        q = deque()
        q.append([0,0,1])
        visit.add((0,0))

        directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1, 1], [-1,-1]]
        while q:
            r,c, length = q.popleft()

            if r < 0 or c < 0 or r == N or c == N or grid[r][c]:
                continue
            if r == N-1 and c == N - 1:
                return length

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row, col) not in visit:
                    q.append([row, col, length + 1])
                    visit.add((row, col))

        return -1