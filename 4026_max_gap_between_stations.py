# nice problem
# may revisit
# greedy earliest and latest
# then merge
class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n, m = len(skill), len(station)
        A, B = [], []
        j = 0
        for i in range(n):
            a = skill[i]
            while station[j] != a:
                j += 1
            A.append(j)
            j += 1
        
        j = m - 1
        for i in range(n-1, -1, -1):
            a = skill[i]
            while station[j] != a:
                j -= 1
            B.append(j)
            j -= 1
        B = B[::-1]
        
        ans = 0
        for (a, b), (c, d) in zip(pairwise(A), pairwise(B)):
            ans = max(ans, b - c, d - a, b - a, d - c)
        return ans