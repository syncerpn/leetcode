# greedy moving with bisect
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        n = len(points)
        P = sorted([x for x, _ in points])
        i = 0
        j = bisect.bisect(P, P[0] + w)
        ans = 1
        while j < n:
            j = bisect.bisect(P, P[j] + w)
            ans += 1
        return ans
