# easy
class Solution:
    def minRotations(self, s: str) -> int:
        ans = 0
        p = 0
        for c in s:
            c = int(c)
            a, b = min(p, c), max(p, c)
            ans += min(b - a, a + 10 - b)
            p = c
        return ans
