# very optimized solution
class Solution:
    def maxDifference(self, s: str) -> int:
        d = Counter(s)
        o, e = 0, float("inf")
        for c, v in d.items():
            if v % 2:
                o = max(o, v)
            else:
                e = min(e, v)
        return o - e