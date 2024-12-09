# this solution is not optimal
# the idea is to build rectangle "side" with one point and its expansion horzly and vertly
# we then check whether the opposite corner exists
# as well as checking if there is any point inside the rectangle
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        ans = -1
        
        points_set = set(tuple(p) for p in points)
        points.sort()
        points_y = sorted(points, key=lambda p: (p[1], p[0]))

        pairs_x = {}
        for a, b in pairwise(points):
            xa, ya = a
            xb, yb = b
            if xa != xb:
                continue
            pairs_x[tuple(a)] = b

        for a, b in pairwise(points_y):
            xa, ya = a
            xb, yb = b
            if ya != yb:
                continue
            if tuple(a) not in pairs_x:
                continue
            xc = xb
            yc = pairs_x[tuple(a)][1]
            if (xc, yc) not in points_set:
                continue
            for i in range(xa, xc+1):
                for j in range(ya, yc+1):
                    if (i == xa and j == ya) or (i == xa and j == yc) or (i == xc and j == ya) or (i == xc and j == yc):
                        continue
                    if (i, j) in points_set:
                        break
                else:
                    continue
                break
            else:
                ans = max(ans, (yc - ya) * (xc - xa))

        return ans