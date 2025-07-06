# thought of union-find
# but actually
# dont really need that
# just bfs/dfs to group and assign each station to an id
# sort it
# for each query, pop-check when a station goes offline
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        g, s, r = {}, {}, {}
        d = [True] * (c + 1)
        for a, b in connections:
            if a not in g:
                g[a] = []
            g[a].append(b)
            if b not in g:
                g[b] = []
            g[b].append(a)

        for a in range(1, c+1):
            if a in r:
                continue
            s[a] = [a]
            r[a] = a
            if a not in g:
                continue
            p = g[a]
            while p:
                b = p.pop()
                if b in r:
                    continue
                r[b] = a
                s[a].append(b)
                if b in g:
                    p += g[b]
            s[a].sort(reverse=True)
        
        ans = []
        for op, a in queries:
            if op == 2:
                d[a] = False
                pa = r[a]
                while s[pa] and not d[s[pa][-1]]:
                    s[pa].pop()
            elif op == 1:
                if d[a]:
                    ans.append(a)
                else:
                    pa = r[a]
                    if s[pa]:
                        ans.append(s[pa][-1])
                    else:
                        ans.append(-1)
        return ans