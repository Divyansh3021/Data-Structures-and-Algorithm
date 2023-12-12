#---------------Problem: 1514----------------

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, des = edges[i]
            adj[src].append([des, succProb[i]])
            adj[des].append([src, succProb[i]])
        
        visit = set()
        priQueue = [[-1, start_node]]

        while priQueue:
            prob, curr = heappop(priQueue)

            visit.add(curr)

            if curr == end_node:
                return -1 * prob
            
            for nei, edgeProb in adj[curr]:
                if nei not in visit:
                    heappush(priQueue, [prob * edgeProb, nei])
        return 0