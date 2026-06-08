# easy
class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        k = brightness // 3 + int(brightness % 3 > 0)
        ans = 0
        intervals.sort()
        p, q = intervals[0]
        for a, b in intervals:
            if a <= q:
                q = max(b, q)
            else:
                ans += (q - p + 1) * k
                p, q = a, b
        ans += (q - p + 1) * k
        return ans