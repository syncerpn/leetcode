# dfs
# but with memoi, it is a dp solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        @functools.cache
        def test(i, j):
            if j == n:
                return m - i
            elif i == m:
                return n - j
            elif word1[i] == word2[j]:
                return test(i+1, j+1)
            return 1 + min(test(i+1, j+1), test(i, j+1), test(i+1, j))
            
        return test(0, 0)

# revisited with https://usaco.guide/CPH.pdf
# classic dp problem
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            a = word1[i-1]
            for j in range(1, n + 1):
                b = word2[j-1]
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + int(a != b))
        return dp[m][n]