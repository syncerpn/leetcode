# binary search
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        s = [(a, b, i) for i, (a, b) in enumerate(intervals)]
        s.sort()
        ans = [-1] * n
        for i in range(n):
            _, b = intervals[i]
            j = bisect.bisect_right(s, (b, -inf, -1))
            if j == n:
                ans[i] = -1
            else:
                ans[i] = s[j][2]
        return ans