#----------------Problem: 2492----------------
#----------T.C. = O(n)--------------
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))

        def dfs(node):
            if node in visit:
                return
            
            nonlocal res
            visit.add(node)
            for nei, dist in adj[node]:
                res = min(res, dist)
                dfs(nei)

        res = float("inf")
        visit = set()
        dfs(1)
        return res