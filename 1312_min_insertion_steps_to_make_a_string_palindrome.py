# lcs of s and inverse of s
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for j in range(n+1)] for i in range(n+1)]
        for i in range(n):
            p = s[i]
            for j in range(n):
                q = s[-1-j]
                if p == q:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return n - dp[-1][-1]
        