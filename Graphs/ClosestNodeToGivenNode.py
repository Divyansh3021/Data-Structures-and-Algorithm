#---------------Problem: 2359--------------

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = collections.defaultdict(list)
        for i, dst in enumerate(edges):
            adj[i].append(dst)
        
        def bfs(src, distMap):
            q = deque()
            q.append([src, 0])
            distMap[src] = 0

            while q:
                node, dist = q.popleft()
                for neighbor in adj[node]:
                    if neighbor not in distMap:
                        q.append([neighbor, dist + 1])
                        distMap[neighbor] = dist + 1

        dist1Map = {}
        dist2Map = {}
        bfs(node1, dist1Map)
        bfs(node2, dist2Map)

        res = -1
        maxDist = float("inf")

        for i in range(len(edges)):
            if i in dist1Map and i in dist2Map:
                dist = max(dist1Map[i], dist2Map[i])
                if dist < maxDist:
                    res = i
                    maxDist = dist
        
        return res