# easy
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = defaultdict(int)
        for t in time:
            t %= 60
            d[t] += 1
        
        ans = 0
        for t in d:
            v = d[t]
            if t == 0 or t == 30:
                ans += v * (v - 1) // 2
            elif t < 30 and (60 - t) in d:
                ans += v * d[60 - t]
        return ans