# it is dijkstra obviously
# somehow i used implementation of #3243
# which messed up the order (d, a) by (a, d)
# and made everything wrong at first
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        def bfs(s, e):
            h = [(-1, s)]            
            v = [False] * n
            while h:
                d, a = heapq.heappop(h)
                if a == e:
                    return abs(d)
                if v[a]:
                    continue
                v[a] = True
                if a in g:
                    for b in g[a]:
                        if not v[b]:
                            heapq.heappush(h, (d * g[a][b], b))
            return 0

        g = {}
        for edge, p in zip(edges, succProb):
            a, b = edge
            if a not in g:
                g[a] = {}
            g[a][b] = p
            if b not in g:
                g[b] = {}
            g[b][a] = p

        return bfs(start_node, end_node)