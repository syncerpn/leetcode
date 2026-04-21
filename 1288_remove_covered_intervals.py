# line sweep just by sorting
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        c, d = intervals[0]
        ans = 1
        for a, b in intervals[1:]:
            if b <= d:
                continue
            c, d = a, b
            ans += 1
        return ans
