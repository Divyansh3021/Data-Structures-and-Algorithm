#-------------Problem: 2477------------

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)

        for src, des in roads:
            adj[src].append(des)
            adj[des].append(src)
        
        fuel = 0

        def dfs(node, parent):
            nonlocal fuel
            passengers = 0
            for child in adj[node]:
                if child != parent:
                    p = dfs(child,node)
                    passengers += p
                    fuel += int(ceil(p/seats))
            return passengers + 1
        
        dfs(0, -1)
        return fuel