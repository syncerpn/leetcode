# union-find solution
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g = {i: i for i in range(n)}
        def find(x):
            while x != g[x]:
                x = g[x]
            return x
        
        def union(x, y):
            px = find(x)
            py = find(y)
        
            g[y] = px

        for u, v in edges:
            if find(v) != find(u):
                union(u, v)
        
        s = find(0)
        for i in range(n):
            if s != find(i):
                return -1
        return s

# but it could actually be this easy
# just find the one with so-called zero-indegree
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weak = {b for a, b in edges}
        return -1 if len(weak) < n - 1 else n * (n - 1) // 2 - sum(weak)