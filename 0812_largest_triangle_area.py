# brute-force O(n3) is fine
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        a_max = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    x1,y1 = points[i]
                    x2,y2 = points[j]
                    x3,y3 = points[k]
                    a = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    a_max = a if a > a_max else a_max
        
        return a_max

# the following solution is optimized
# copied from leetcode solution
# ref paper: https://arxiv.org/pdf/1705.11035.pdf
# basically, we try to build a convex hull from the given point list
# it is proven that triangle with max area should has its points on the hull
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangle_area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
        
        # Function to compute the convex hull using Andrew's monotone chain algorithm
        def convex_hull(points):
            points = sorted(points)
            
            # Build the lower hull
            lower = []
            for p in points:
                while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                    lower.pop()
                lower.append(p)
            
            # Build the upper hull
            upper = []
            for p in reversed(points):
                while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                    upper.pop()
                upper.append(p)
            
            # Remove the last point of each half because it's repeated at the beginning of the other half
            return lower[:-1] + upper[:-1]
        
        # Cross product of vectors OA and OB
        # A positive cross product indicates a counter-clockwise turn, negative indicates a clockwise turn, and zero indicates a collinear point
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        # Compute the convex hull
        hull = convex_hull(points)
        
        # Find the largest triangle area from the convex hull
        max_area = 0
        for p1, p2, p3 in itertools.combinations(hull, 3):
            max_area = max(max_area, triangle_area(p1, p2, p3))
        
        return max_area