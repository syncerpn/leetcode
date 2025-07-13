# similar to 3613
# we can use binary search
# or use union-find + sorting for faster processing speed
class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
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

        edges.sort(key = lambda e: -e[2])
        c = n
        f = list(range(n))
        for u, v, t in edges:
            if union(u, v):
                c -= 1
            if c < k:
                return t
        return 0