# solved it myself
# build a graph then distance graph
# then simply connect each node of the first tree to the one with most k-1 targets
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def dfs(gk, dk, a, v):
            v.add(a)
            p = set([a])
            for b in gk[a]:
                if b in v:
                    continue
                
                v.add(b)
                dk[a][b] = 1
                dk[b][a] = 1
                q = dfs(gk, dk, b, v)
                for i in q:
                    dk[a][i] = dk[a][b] + dk[b][i]
                    dk[i][a] = dk[a][i]
                    for j in p:
                        dk[i][j] = dk[a][i] + dk[a][j]
                        dk[j][i] = dk[a][j] + dk[a][i]
                q.add(b)
                p |= q
            return p

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
        d = [[[0] * m for _ in range(m)], [[0] * n for _ in range(n)]]

        dfs(g[0], d[0], 0, set())
        dfs(g[1], d[1], 0, set())

        g1_node_best = max([sum(dij <= k-1 for dij in di) for di in d[1]])
        return [g1_node_best + sum(dij <= k for dij in di) for di in d[0]]