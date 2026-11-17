# easy
class Solution:
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
        g = {}
        for c, p in enumerate(parent):
            if p == -1:
                continue
            if p not in g:
                g[p] = []
            g[p].append(c)
        
        def helper(p):
            m = inf
            q = score[p]
            ans = 0
            if p not in g:
                m = 0
            else:
                for c in g[p]:
                    s = helper(c)
                    m = min(m, s)
                    q += s
            
            if op[p] == 0 and m >= 0:
                return q
            return q - m
        
        return helper(0)