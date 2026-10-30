# update 261030
# new test cases added which make me reconsider path with an already visited node
# because revisiting a node with fewer consecutive char count can be a valid solution
# the condition f[v] <= mm enliminates those candidates that revisits a node with a higher weight while consecutive char count is closer to k
# which is just worse than previously tried candidates and definitely will not work
# therefore, we can safely skip them
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = {}
        for u, v, w in edges:
            if u not in g:
                g[u] = []
            g[u].append((v, w))
        
        f = [inf] * n
        h = [(0, 0, labels[0], 1)]
        while h:
            w, u, c, m = heapq.heappop(h)
            if u == n - 1:
                return w
            if f[u] <= m:
                continue
            f[u] = m
            if u in g:
                for v, z in g[u]:
                    d = labels[v]
                    mm = m + 1 if d == c else 1
                    if (d == c and m == k) or f[v] <= mm:
                        continue
                    heapq.heappush(h, (w + z, v, d, mm))
        
        return -1

# the following is a previously wrong solution considering only visited node
# which falls for the newly added test cases no.1000 and no.1001
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