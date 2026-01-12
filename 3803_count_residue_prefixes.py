# easy
class Solution:
    def residuePrefixes(self, s: str) -> int:
        v = set()
        ans = 0
        for i, c in enumerate(s):
            if c not in v:
                v.add(c)
            if len(v) == (i + 1) % 3:
                ans += 1
            elif len(v) > 2:
                break
        return ans