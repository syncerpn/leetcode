# construct graph first
# then bfs to find all connected components
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n, m = len(properties), len(properties[0])
        g = [[0] * n for _ in range(n)]
        d = {}
        for i, p in enumerate(properties):
            for a in set(p):
                if a not in d:
                    d[a] = []
                for j in d[a]:
                    g[i][j] += 1
                    g[j][i] += 1
                d[a].append(i)
        
        for i in range(n):
            g[i] = [j for j in range(n) if g[i][j] >= k]
        
        ans = 0
        v = set(list(range(n)))
        while v:
            s = deque([v.pop()])
            while s:
                i = s.popleft()
                for j in g[i]:
                    if j in v:
                        s.append(j)
                        v.discard(j)
            ans += 1
        return ans

# maybe bitcount, bitmask, and & operator could improve the speed