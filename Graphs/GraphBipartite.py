#----------Problem: 785----------

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visit = [0] * len(graph)

        def bfs(i):
            if visit[i]:
                return True

            q = deque([i])
            visit[i] = -1

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if visit[nei] == visit[node]:
                        return False
                    elif not visit[nei]:
                        q.append(nei)
                        visit[nei] = -1 * visit[node]
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True