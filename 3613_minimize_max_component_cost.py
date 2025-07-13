# binary search + dfs
class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if n <= k:
            return 0
        g = {}
        l, r = 0, -float("inf")
        for a, b, w in edges:
            if a not in g:
                g[a] = {}
            g[a][b] = w
            if b not in g:
                g[b] = {}
            g[b][a] = w
            r = max(r, w)
        
        def validate(m):
            c = 0
            v = set(list(range(n)))
            while v:
                s = [v.pop()]
                while s:
                    a = s.pop()
                    for b in g[a]:
                        if b in v and g[a][b] <= m:
                            s.append(b)
                            v.remove(b)
                c += 1
            return c <= k
        
        while l < r - 1:
            m = (l + r) // 2
            if validate(m):
                r = m
            else:
                l = m
        
        return r

# super-fast union-find approach, no binary search needed
# because we sort the edges by their weights first
class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        p = {i:i for i in range(n)}
        def find(x):
            if x == f[x]:
                return x
            f[x] = find(f[x])
            return f[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            f[x] = y
            return True
        
        if n <= k:
            return 0
        
        edges.sort(key=lambda e: e[2])
        c = n
        f = list(range(n))
        for a, b, w in edges:
            if union(a, b):
                c -= 1
            if c <= k:
                return w