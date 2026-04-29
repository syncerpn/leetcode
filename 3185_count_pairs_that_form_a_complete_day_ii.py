# easy
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        d = {h: 0 for h in range(24)}
        for h in hours:
            hh = h % 24
            if hh not in d:
                d[hh] = 0
            d[hh] += 1
        
        ans = 0
        for h in range(13):
            if h == 12 or h == 0:
                ans += d[h] * (d[h] - 1) // 2
            else:
                ans += d[h] * d[24-h]
        return ans