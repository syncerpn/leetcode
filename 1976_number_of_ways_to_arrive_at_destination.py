# dp + dijkstra
# the key thing is
# how to count the fastest way to reach a node
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        g = [[] for _ in range(n)]
        for a, b, t in roads:
            g[a].append((b, t))
            g[b].append((a, t))
        
        d = [float("inf")] * n
        w = [0] * n

        d[0] = 0
        w[0] = 1

        h = [(0, 0)]
        heapq.heapify(h)
        while h:
            t, a = heapq.heappop(h)
            if t > d[a]:
                continue
            
            for b, t in g[a]:
                if d[a] + t < d[b]:
                    d[b] = d[a] + t
                    w[b] = w[a]
                    heapq.heappush(h, (d[b], b))
                elif d[a] + t == d[b]:
                    w[b] = (w[b] + w[a]) % MOD
        
        return w[n-1]