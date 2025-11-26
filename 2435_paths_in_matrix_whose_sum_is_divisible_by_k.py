# dp
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * n for _ in range(m)] for _ in range(k)]
        for i in range(m):
            for j in range(n):
                g = grid[i][j]
                if i == 0 and j == 0:
                    dp[g % k][0][0] = 1
                if i > 0:
                    for a in range(k):
                        dp[(a+g)%k][i][j] += dp[a][i-1][j]
                if j > 0:
                    for a in range(k):
                        dp[(a+g)%k][i][j] += dp[a][i][j-1]
                for a in range(k):
                    dp[a][i][j] %= MOD
            
        return dp[0][m-1][n-1]