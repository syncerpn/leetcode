# easy bisect, same as before
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        R = sorted([r for _, r in intervals])
        ans = 0
        for i, (l, r) in enumerate(intervals):
            j = bisect.bisect_left(R, l)
            ans += i - j
        return ans