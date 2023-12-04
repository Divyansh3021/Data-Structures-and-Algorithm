#-------------Problem: 1129-------------

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)

        for src, des in redEdges:
            red[src].append(des)
        for src, des in blueEdges:
            blue[src].append(des)

        answer = [-1 for i in range(n)]

        q = deque()
        q.append([0,0, None]) #[Node, length, prev_edge_color]
        visit = set()
        visit.add((0,None))

        while q:
            node, length, prev_edge_color = q.popleft()

            if answer[node] == -1:
                answer[node] = length
            
            if prev_edge_color != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        q.append([nei, length + 1, "RED"])
                        visit.add((nei, "RED"))

            if prev_edge_color != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        q.append([nei, length + 1, "BLUE"])
                        visit.add((nei, "BLUE"))

        return answer