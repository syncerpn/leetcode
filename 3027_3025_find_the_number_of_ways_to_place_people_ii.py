# same optimal solution as #3025
# simply, we want to sort the placements left-to-right then up-to-down
# then pairing them while tracking highest rectange (i.e. y-level) so far
# with point i as base point to pair with
# only point j with y-level lower than point i
# and does not fall into the max y-level, denoted as m, so far
# can be paired with point i
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda p: (p[0],-p[1]))
        ans = 0
        for i in range(n-1):
            _, b = points[i]
            m = -float(inf)
            for j in range(i+1, n):
                _, d = points[j]
                if d <= b and d > m:
                    ans += 1
                    m = d
        return ans