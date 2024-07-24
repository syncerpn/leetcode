# union-find at the first glance
# yet i made mistake implementing the solution
# just because i assign parent to the node instead of its parent
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = {}
        def find(a):
            if a not in d:
                d[a] = a
            
            if a != d[a]:
                d[a] = find(d[a])
            
            return d[a]
        
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa < pb:
                # this is assign to parent of b, which is pb
                # i made mistake assign to b itself: d[b] = pa
                # this is wrong and should never be repeated
                d[pb] = pa
            else:
                d[pa] = pb
        
        for a, b in zip(s1, s2):
            union(a, b)
            
        r = ""
        for c in baseStr:
            r += find(c)
        return r