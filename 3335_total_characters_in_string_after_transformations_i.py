# dp is my love now
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        d = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        MOD = 10 ** 9 + 7
        dp = [0] * (t + 26)
        for i in range(t + 26):
            if i < 26:
                dp[i] = 1
            else:
                dp[i] = (dp[i-25] + dp[i-26]) % MOD
        
        ans = 0
        for c in s:
            ans = (ans + dp[d[c] + t]) % MOD
        return ans