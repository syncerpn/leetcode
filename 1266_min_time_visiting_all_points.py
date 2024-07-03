# just travel
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        for s, d in pairwise(points):
            sx, sy = s
            dx, dy = d
            t += max(abs(dy-sy), abs(dx-sx))
        return t
