# greedy
# always priotize earliest ending time first
# because they would allow more capcity for the rest
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        p = intervals[0][1]
        ans = 0
        for a, b in intervals[1:]:
            if a >= p:
                p = b
            else:
                ans += 1
        return ans