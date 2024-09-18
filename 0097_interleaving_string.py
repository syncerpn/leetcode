# 2d dp is clear
# but it can be optimized to be O(len(s2)) space
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        m, n = len(s1), len(s2)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i-1][j] and s3[i+j-1] == s1[i-1])
                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j-1] and s3[i+j-1] == s2[j-1])
        return dp[m][n]

# here is O(len(s2)) space solution
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        m, n = len(s1), len(s2)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for j in range(1, n+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n+1):
                dp[j] = (dp[j-1] and s3[i+j-1] == s2[j-1]) or (dp[j] and s3[i+j-1] == s1[i-1])
        return dp[n]