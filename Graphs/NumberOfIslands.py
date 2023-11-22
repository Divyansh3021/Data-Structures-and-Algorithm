#--------Problem: 200-----------

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        queue = deque()
        
        def bfs(r, c):
            queue.append((r, c))

            while queue:
                pos = queue.popleft()
                row, col = pos[0], pos[1]

                for row_offset, col_offset in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if (
                        row + row_offset < 0 or
                        row + row_offset >= rows or
                        col + col_offset < 0 or
                        col + col_offset >= cols or
                        grid[row + row_offset][col + col_offset] != "1" or
                        (row + row_offset, col + col_offset) in visited
                    ):
                        continue
                    visited.add((row + row_offset, col + col_offset))
                    queue.append((row + row_offset, col + col_offset))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        return islands

#T: O(M X N)
#S: O(M X N)