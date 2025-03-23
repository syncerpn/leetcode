# union-find solution, was pretty slow though
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        d = {i: 1 for i in range(n)}
        p = {i: i for i in range(n)}

        def find(i):
            if i == p[i]:
                return i
            return find(p[i])
        
        def union(i, j):
            pi = find(i)
            pj = find(j)
            p[pi] = pj
        
        for a, b in edges:
            d[a] += 1
            d[b] += 1
            union(a, b)
        
        g = {}
        ans = 0
        for i in range(n):
            pi = find(i)
            if pi not in g:
                g[pi] = set()
            g[pi].add(i)
        
        return sum(all(d[i] == len(g[pi]) for i in g[pi]) for pi in g)

# bfs solution
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        G = [[] for i in range(n)]
        for i,j in edges:
            G[i].append(j)
            G[j].append(i)
        seen = [0] * n

        res = 0
        for i in range(n):
            if seen[i]: continue
            bfs = [i]
            seen[i] = 1
            for j in bfs:
                for k in G[j]:
                    if seen[k] == 0:
                        bfs.append(k)
                        seen[k] = 1
            if all(len(G[j]) == len(bfs) - 1 for j in bfs):
                res += 1
        return res    
