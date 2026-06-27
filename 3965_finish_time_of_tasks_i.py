# recursive with memoi
# actually, dont really need functools.cache memoi
# just simply store the time into a variable t
# because it is a tree
class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        l = [True] * n
        g = {}
        for a, b in edges:
            if a not in g:
                g[a] = []
            g[a].append(b)
            l[a] = False
        
        def f(a):
            if l[a]:
                return baseTime[a]
            mi, ma = inf, -inf
            for b in g[a]:
                t = f(b)
                mi = min(mi, t)
                ma = max(ma, t)
            return ma * 2 - mi + baseTime[a]
        
        return f(0)