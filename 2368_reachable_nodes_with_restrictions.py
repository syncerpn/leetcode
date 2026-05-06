# simple traversal
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        g = {}
        for a, b in edges:
            if a not in g:
                g[a] = []
            g[a].append(b)
            if b not in g:
                g[b] = []
            g[b].append(a)
        
        s = [0]
        v = set([0])
        while s:
            a = s.pop()
            for b in g[a]:
                if b not in v and b not in restricted:
                    s.append(b)
                    v.add(b)
        
        return len(v)