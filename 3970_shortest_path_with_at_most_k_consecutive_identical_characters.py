# dijkstra
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = {}
        for u, v, w in edges:
            if u not in g:
                g[u] = []
            g[u].append((v, w))
        
        f = [False] * n
        h = [(0, 0, labels[0], 1)]
        while h:
            w, u, c, m = heapq.heappop(h)
            if u == n - 1:
                return w
            if f[u]:
                continue
            f[u] = True
            if u in g:
                for v, z in g[u]:
                    d = labels[v]
                    if (d == c and m == k) or f[v]:
                        continue
                    heapq.heappush(h, (w + z, v, d, (m + 1) if d == c else 1))
        
        return -1