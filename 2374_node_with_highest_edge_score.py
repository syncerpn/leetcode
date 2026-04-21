# easy
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        ans, ma = 0, 0
        d = [0] * len(edges)
        for i, a in enumerate(edges):
            d[a] += i
            if ma < d[a]:
                ma = d[a]
                ans = a
            elif ma == d[a] and a < ans:
                ans = a
        
        return ans