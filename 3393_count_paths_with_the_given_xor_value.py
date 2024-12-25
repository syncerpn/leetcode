# dp obviously
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[{} for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = 1
        dp[m-1][n-1][k] = 0
        for i in range(m):
            for j in range(n):
                a = grid[i][j]
                if i == 0 and j == 0: continue
                if i > 0:
                    for c in dp[i-1][j]:
                        b = c ^ a
                        if b not in dp[i][j]:
                            dp[i][j][b] = 0
                        dp[i][j][b] += dp[i-1][j][c]
                        
                if j > 0:
                    for c in dp[i][j-1]:
                        b = c ^ a
                        if b not in dp[i][j]:
                            dp[i][j][b] = 0
                        dp[i][j][b] += dp[i][j-1][c]
        return dp[m-1][n-1][k] % (10 ** 9 + 7)