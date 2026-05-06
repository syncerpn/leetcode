# easy
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        l = 1
        ans = 1
        for a, b in pairwise(s):
            if b == a:
                l += 1
            else:
                l = 1
            ans += l
        return ans % MOD