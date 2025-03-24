# memory constraint does not allow line sweep
# so just use merge interval instead
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        s, e = 0, 0
        ans = 0
        for a, b in meetings:
            if a > e:
                ans += a - e - 1
                s = a
            if b > e:
                e = b
        ans += days - e
        return ans