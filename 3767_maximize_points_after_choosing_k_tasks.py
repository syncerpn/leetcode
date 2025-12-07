# fairly easy
class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        g = [(b - a, i) for i, (a, b) in enumerate(zip(technique1, technique2))]
        g.sort()
        ans = 0
        for j, (p, i) in enumerate(g):
            if j < k or p < 0:
                ans += technique1[i]
            else:
                ans += technique2[i]
        
        return ans