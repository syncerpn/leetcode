# good reduction from O(mn2) to O(mn)
# by building 2 more dp tables for each row
# the dp tables, l and r are max value for choosing prev points[i-1][k]
# all the costs are calculated and put into those two tables
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        p = points[0][:]
        for i in range(1, m):
            l = [p[0]] + [0 for _ in range(n-1)]
            r = [0 for _ in range(n-1)] + [p[-1]]
            for j in range(1, n):
                l[j] = max(l[j-1]-1, p[j])
            
            for j in range(n-2,-1,-1):
                r[j] = max(r[j+1]-1, p[j])
            
            for j in range(n):
                p[j] = points[i][j] + max(l[j], r[j])
        
        return max(p)