#-------------Problem: 1631-----------

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        visit = set()
        minHeap = [[0, 0, 0]] #[maxAbsDiff, r, c]
        direc = [[1,0], [-1,0], [0,1], [0,-1]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r,c) in visit:
                continue
            visit.add((r,c))

            if (r,c) == (ROWS-1, COLS-1):
                return diff
            
            for dr, dc in direc:
                newR, newC = r + dr, c + dc

                if newR < 0 or newC < 0 or newR == ROWS or newC == COLS or (newR, newC) in visit:
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])