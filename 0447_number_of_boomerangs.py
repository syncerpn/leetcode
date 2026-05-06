# simple pairwise
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for a in points:
            xa, ya = a
            g = defaultdict(int)
            for b in points:
                xb, yb = b
                d = (xa - xb) ** 2 + (ya - yb) ** 2
                ans += g[d]
                g[d] += 1
        return ans * 2