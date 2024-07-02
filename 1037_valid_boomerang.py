# use line formula
# or you can try triangle area formula in #0812
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        if x0 == x1 == x2 or y0 == y1 == y2:
            return False

        return (x1 - x0) * (y2 - y0) != (y1 - y0) * (x2 - x0)