# easy
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        l = 1
        for a, b in pairwise(s):
            if ord(b) - ord(a) == 1:
                l += 1
                ans = max(ans, l)
            else:
                l = 1
        return ans