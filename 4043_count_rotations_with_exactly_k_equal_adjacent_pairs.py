# easy
class Solution:
    def countRotations(self, s: str, k: int) -> int:
        r = 0
        for a, b in pairwise(s):
            if a == b:
                r += 1
        ans = int(r == k)
        for i in range(len(s) - 1):
            rr = r - int(s[i] == s[i+1]) + int(s[0] == s[-1])
            if rr == k:
                ans += 1
        return ans