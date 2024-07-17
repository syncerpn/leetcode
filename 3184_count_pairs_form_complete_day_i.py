# turn them into remainder of 24
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        d = {}
        for h in hours:
            r = h % 24
            if r not in d:
                d[r] = 0
            d[r] += 1
        
        c = 0
        for r in d:
            if r > 12:
                continue
            if r == 0 or r == 12:
                c += d[r] * (d[r] - 1) // 2
            elif 24 - r in d:
                c += d[r] * d[24 - r]
        return c