# counting
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        
        for c in t:
            if c not in d:
                return c
            d[c] -= 1
            if d[c] < 0:
                return c