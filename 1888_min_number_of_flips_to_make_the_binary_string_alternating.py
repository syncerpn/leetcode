# sliding window
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        f0, f1 = 0, 0
        ans = inf
        for i, c in enumerate(s):
            if i >= n:
                ans = min(ans, f0, f1)
                f0 -= int(s[i-n]) != (i-n) % 2
                f1 -= int(s[i-n]) == (i-n) % 2
            f0 += int(c) != i % 2
            f1 += int(c) == i % 2
        return ans
