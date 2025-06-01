# easier than the previous version actually
# also same logic
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(gk, dk, a, v):
            v.add(a)
            for b in gk[a]:
                if b in v:
                    continue
                v.add(b)
                dk[b] = not dk[a]
                dfs(gk, dk, b, v)

        g = [{}, {}]
        for i, edges in enumerate([edges1, edges2]):
            for a, b in edges:
                if a not in g[i]:
                    g[i][a] = []
                g[i][a].append(b)
                
                if b not in g[i]:
                    g[i][b] = []
                g[i][b].append(a)
        
        m, n = len(g[0]), len(g[1])
        d = [[True] * m, [True] * n]

        dfs(g[0], d[0], 0, set())
        dfs(g[1], d[1], 0, set())
        
        g1_node_best = max(sum(d[1]), n - sum(d[1]))
        print(g1_node_best)
        g0_t = sum(d[0])
        g0_f = m - g0_t
        return [g1_node_best + (g0_t if d[0][i] else g0_f) for i in range(m)]