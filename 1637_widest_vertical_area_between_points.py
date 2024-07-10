# more like horizontal distance lol
# description is overcomplicated
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        d = 0
        for a, b in pairwise(points):
            d = max(b[0] - a[0], d)
        return d