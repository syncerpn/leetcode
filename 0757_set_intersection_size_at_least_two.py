# greedy tracking 2 right-most points
# might need revisit
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        ans = 0
        v = []
        for s, e in intervals:
            if not v or s > v[1]:
                ans += 2
                v = [e-1, e]
            elif s > v[0]:
                ans += 1
                v = [v[1], e]
        return ans
        