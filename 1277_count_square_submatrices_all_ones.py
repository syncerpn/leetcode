# dynamic programming
# trying to log square size into dp table
# such that dp[i][j] is the size s of biggest square matrix[i-s+1:i][j-s+1:j]
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)
                ans += dp[i][j]
        
        return ans