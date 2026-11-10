# easy
class Solution:
    def countValidSubstrings(self, s: str) -> int:
        l = 0
        ans = 0
        for r, c in enumerate(s):
            if r - l >= 2 and s[r-2:r+1] == "abc":
                l = r - 1
            ans += r - l + 1
        return ans