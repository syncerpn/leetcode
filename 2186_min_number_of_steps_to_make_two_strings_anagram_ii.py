# simple counting
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        for c in t:
            if c not in d:
                d[c] = 0
            d[c] -= 1
        ans = 0
        for c in d:
            ans += abs(d[c])
        return ans