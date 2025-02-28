# simply find the longest common subsequence of the str1 and str2 by dp
# then trace back and build the supersequence from the non-common and common characters
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        ans = ""
        i, j = m, n
        while i > 0 and j > 0:
            if dp[i-1][j-1] == dp[i-1][j] == dp[i][j-1] == dp[i][j]-1:
                ans += str1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                ans += str1[i-1]
                i -= 1
            else:
                ans += str2[j-1]
                j -= 1
        
        return str1[:i] + str2[:j] + ans[::-1]

# actually, dont have to trace back, but we can go from the first to the last with the dp