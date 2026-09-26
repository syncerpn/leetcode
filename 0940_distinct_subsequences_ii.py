# nice math
# need revisit
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        tot = 0
        dp = [0] * 26

        for c in s:
            c = ord(c) - 97
            new = tot + 1 - dp[c]
            tot = (tot + new) % MOD
            dp[c] = (dp[c] + new) % MOD

        return tot 
        