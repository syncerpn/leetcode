# easy
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        d = 0
        ans = 0
        for c in s:
            if c == "0":
                d += 1
            else:
                d -= 1
            ans += abs(d) < 2
        return ans