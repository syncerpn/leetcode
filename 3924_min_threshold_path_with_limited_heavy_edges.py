# binary search + djikstra at the first sight
# very doable hard prob
class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
        def traverse(t):
            q = [False] * n
            h = [(0, source)]
            while h:
                c, u = heapq.heappop(h)
                if q[u]:
                    continue
                q[u] = True
                if u == target:
                    return True
                for v in g[u]:
                    if q[v]:
                        continue
                    if g[u][v] > t:
                        if c < k:
                            heapq.heappush(h, (c + 1, v))
                    else:
                        heapq.heappush(h, (c, v))
            return False

        g = defaultdict(defaultdict)
        l, r = 0, -inf
        for u, v, w in edges:
            if v not in g[u]:
                g[u][v] = w
            g[u][v] = min(w, g[u][v])
            if u not in g[v]:
                g[v][u] = w
            g[v][u] = min(w, g[v][u])
            r = max(r, w)
        
        if not traverse(r):
            return -1

        while l < r:
            m = (l + r) // 2
            if traverse(m):
                r = m
            else:
                l = m + 1
        return r

# learned a trick with bisect
# this will sooth my binary search implementation next time
class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
        def traverse(t):
            q = [False] * n
            h = [(0, source)]
            while h:
                c, u = heapq.heappop(h)
                if q[u]:
                    continue
                q[u] = True
                if u == target:
                    return True
                for v in g[u]:
                    if q[v]:
                        continue
                    if g[u][v] > t:
                        if c < k:
                            heapq.heappush(h, (c + 1, v))
                    else:
                        heapq.heappush(h, (c, v))
            return False

        g = defaultdict(defaultdict)
        W = []
        for u, v, w in edges:
            if v not in g[u]:
                g[u][v] = w
            g[u][v] = min(w, g[u][v])
            if u not in g[v]:
                g[v][u] = w
            g[v][u] = min(w, g[v][u])
            W.append(w)
        
        W.sort()
        i = bisect_left(W, True, key=traverse)
        return W[i] if i < len(W) else -1