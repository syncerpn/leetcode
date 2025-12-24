# easy
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        d = {}
        m = 0
        for i, c in enumerate(s):
            if c not in d:
                d[c] = 0
            d[c] += cost[i]
            m += cost[i]
        
        return m - max(d.values())