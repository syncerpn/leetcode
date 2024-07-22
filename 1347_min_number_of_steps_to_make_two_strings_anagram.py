# pure counting
# should be easy problem instead of medium
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1

        r = 0
        for c in t:
            if c not in d or d[c] == 0:
                r += 1
            else:
                d[c] -= 1
        return r