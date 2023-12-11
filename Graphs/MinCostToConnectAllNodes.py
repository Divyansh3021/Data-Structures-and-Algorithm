#-----------------Problem: 1584-----------------

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        #Prim's Algo
        minHeap = [[0,0]]
        visit = set()
        res = 0

        while len(visit) < N:
            cost, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            visit.add(node)
            res += cost
            for neiCost, nei in adj[node]:
                if nei in visit:
                    continue
                heapq.heappush(minHeap, [neiCost, nei])
        
        return res