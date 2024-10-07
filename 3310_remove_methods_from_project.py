# with dfs seems fine
# this is my solution during the contest
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = {}
        r = {}
        for a, b in invocations:
            if a not in g:
                g[a] = set()
            g[a].add(b)
            if b not in r:
                r[b] = set()
            r[b].add(a)
        
        s = [k]
        v = set()
        while s:
            a = s.pop()
            if a in v:
                continue
            v.add(a)
            if a in g:
                for b in g[a]:
                    s.append(b)
        
        ans = set(list(range(n)))
        for a in v:
            if a in r:
                for b in r[a]:
                    if b not in v:
                        return list(range(n))
            ans.discard(a)
        
        return ans