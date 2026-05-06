# easy
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d = defaultdict(int)
        for a, b in rectangles:
            d[b/a] += 1
        ans = 0
        for r in d:
            ans += d[r] * (d[r] - 1) // 2
        return ans