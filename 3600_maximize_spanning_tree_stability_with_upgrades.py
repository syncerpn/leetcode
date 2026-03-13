# kruskal + dsu
# need revisit
# can also be solved with binary search
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        used = 0
        ans = inf
        dsu = DSU(n)

        for u, v, s, m in edges:
            if m:
                if not dsu.union(u, v):
                    return -1
                used += 1
                ans = min(ans, s)
        
        edges.sort(key=lambda e: -e[2])
        weights = []
        for u, v, s, m in edges:
            if m == 0:
                if dsu.union(u, v):
                    used += 1
                    weights.append(s)

        for i in range(min(k, len(weights))):
            weights[~i] *= 2

        if used != n - 1:
            return -1
        return min((ans, *weights))


class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True