# simple
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        n = 0
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
            n = d[c]

        for k in d:
            if d[k] != n:
                return False
        return True