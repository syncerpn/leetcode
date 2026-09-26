# dp obviously
# took me quite some time to write the code
# because im just bad
# also space opt is available
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(n+1):
            dp[j][0] = 0
        
        for i in range(m+1):
            dp[0][i] = 1

        for j in range(1, n+1):
            a = t[j-1]
            for i in range(1, m+1):
                b = s[i-1]
                dp[j][i] = dp[j][i-1]
                if a == b:
                    dp[j][i] += dp[j-1][i-1]
        return dp[n][m]