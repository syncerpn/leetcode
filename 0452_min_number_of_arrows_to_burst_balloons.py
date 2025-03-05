# greedy overlapping intervals
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        p, q = points[0]
        ans = 1
        for a, b in points[1:]:
            if a > q:
                ans += 1
                p, q = a, b
            else:
                p = max(p, a)
                q = min(q, b)
        
        return ans

# but this can be further simplified, trimming away unnecessary computation
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        p = points[0][1]
        ans = 1
        for a, b in points[1:]:
            if a > p:
                ans += 1
                p = b
        
        return ans

# somewhat the same
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        p = -float("inf")
        ans = 0
        for a, b in points:
            if a > p:
                ans += 1
                p = b
        
        return ans
