# also, the thing i kept thinking about was
# how to make sure we do not over-use the switch
# but it turns out to be quite easy
# that we just add another edge with double the cost
# and make sure a node is visited only once
# like a normal djikstra, nothing more
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = {}
        for u, v, w in edges:
            if u not in g:
                g[u] = {}
            if v not in g[u]:
                g[u][v] = float("inf")
            g[u][v] = min(g[u][v], w)
            if v not in g:
                g[v] = {}
            if u not in g[v]:
                g[v][u] = float("inf")
            g[v][u] = min(g[v][u], 2 * w)
        
        visited_g = [False] * n
        
        h = [(0, 0)]
        while h:
            c, u = heapq.heappop(h)
            if u == n-1:
                return c
            if visited_g[u]:
                continue
            
            visited_g[u] = True
            if u not in g:
                continue
            for v in g[u]:
                if visited_g[v]:
                    continue
                heapq.heappush(h, (c + g[u][v], v))

        return -1