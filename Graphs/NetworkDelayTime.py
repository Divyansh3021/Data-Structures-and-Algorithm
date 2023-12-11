#---------------Problem: 743--------------

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append([v,w])

        visit = set()
        time = 0
        minHeap = [[0,k]]

#-----------Dijkstra's Algo-------------------
        while minHeap:
            t1, n1 = heappop(minHeap)

            if n1 in visit:
                continue
            time = max(time, t1)
            visit.add(n1)
            for nei, transTime in adj[n1]:
                if nei in visit:
                    continue
                heappush(minHeap, [t1 + transTime, nei])
        return time if len(visit) == n else -1