# fairly easy
# union-find may also work
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = {}
        for a, b, c in roads:
            if a not in g:
                g[a] = []
            g[a].append((b, c))
            if b not in g:
                g[b] = []
            g[b].append((a, c))
        
        v = [False] * n
        v[0] = True

        s = deque([1])
        ans = inf
        while s:
            a = s.popleft()
            if a in g:
                while g[a]:
                    b, c = g[a].pop()
                    ans = min(ans, c)
                    if v[b-1]:
                        continue
                    v[b-1] = True
                    s.append(b)
        return ans