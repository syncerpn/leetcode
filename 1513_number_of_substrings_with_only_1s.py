# easy
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        for a, c in groupby(s):
            if a == "1":
                l = len(list(c))
                ans += (l * (l + 1) // 2) % MOD
        return ans % MOD