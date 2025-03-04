# simple way to think: longest common subsequence of s and its reversed s[::-1]
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if s[i] == s[-1-j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[n][n]

# space optimized
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n+1) for _ in range(2)]
        for i in range(n):
            for j in range(n):
                if s[i] == s[-1-j]:
                    dp[(i+1)%2][j+1] = dp[i%2][j] + 1
                else:
                    dp[(i+1)%2][j+1] = max(dp[(i+1)%2][j], dp[i%2][j+1])
        
        return dp[n%2][n]