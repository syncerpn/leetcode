# easy
class Solution:
    def maxFreqSum(self, s: str) -> int:
        V = "aeiou"
        d = Counter(s)
        v, c = 0, 0
        for a in d:
            if a in V:
                v = max(v, d[a])
            else:
                c = max(c, d[a])
        return v + c
