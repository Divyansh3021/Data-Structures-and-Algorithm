#------------------Problem: 778----------------------

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        priQueue = [[grid[0][0], 0, 0]]         #[time, row, col]
        visit = set()
        visit.add((0,0))

        direct = [[1,0], [-1,0], [0,1], [0,-1]]
        while priQueue:
            time, row, col = heappop(priQueue)
            if row == ROWS -1 and col == COLS-1:
                return time

            for dr, dc in direct:
                newR, newC = row + dr, col + dc
                if newR < 0 or newC < 0 or newR == ROWS or newC == COLS or (newR, newC) in visit:
                    continue
                visit.add((newR, newC))
                newTime = max(time, grid[newR][newC])
                heappush(priQueue, [newTime, newR, newC])
