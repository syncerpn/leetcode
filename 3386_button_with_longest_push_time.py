# easy
class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        d = {}
        ans = events[0][0]
        d[ans] = events[0][1]
        for a, b in pairwise(events):
            _, m = a
            i, n = b
            if i not in d:
                d[i] = 0
            d[i] = max(d[i], n - m)
            if d[i] > d[ans]:
                ans = i
            elif d[i] == d[ans]:
                ans = min(ans, i)
        return ans