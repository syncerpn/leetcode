# fairly easy
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = sorted([list(map(int, p.split(":"))) for p in timePoints])
        ans = 60 * (timePoints[0][0] - timePoints[-1][0]) + timePoints[0][1] - timePoints[-1][1] + 1440
        for a, b in pairwise(timePoints):
            ans = min(ans, 60 * (b[0] - a[0]) + b[1] - a[1])
        return ans