# easy
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        g = {}
        for i, p in enumerate(parent):
            if p == -1:
                continue
            if p not in g:
                g[p] = []
            g[p].append(i)
        s = [(0, 0)]
        ans = 0
        t = 0
        h = 0
        while s:
            p, d = s.pop()
            ans += nums[p] * (1 - d)
            t += nums[p]
            h = max(h, d)
            if p in g:
                for a in g[p]:
                    s.append((a, d + 1))
        
        return t * h + ans