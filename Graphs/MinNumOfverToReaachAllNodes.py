#---------------Problem: 1557---------------

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        res = []

        for src, des in edges:
            adj[des].append(src)

        for i in range(n):
            if not adj[i]:
                res.append(i)

        return res