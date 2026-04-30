# tried djikstra but got memory limit
# need dp
# crazy runtime though
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-inf for _ in range(k+1)] for _ in range(n)] for _ in range(m)]
        dp[0][0][int(grid[0][0] > 0)] = grid[0][0]
        for j in range(1, n):
            c = int(grid[0][j] > 0)
            for kk in range(c, k+1):
                if dp[0][j-1][kk-c] > -inf:
                    dp[0][j][kk] = dp[0][j-1][kk-c] + grid[0][j]
        
        for i in range(1, m):
            c = int(grid[i][0] > 0)
            for kk in range(c, k+1):
                if dp[i-1][0][kk-c] > -inf:
                    dp[i][0][kk] = dp[i-1][0][kk-c] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                c = int(grid[i][j] > 0)
                for kk in range(c, k+1):
                    if dp[i-1][j][kk-c] > -inf:
                        dp[i][j][kk] = max(dp[i][j][kk], dp[i-1][j][kk-c] + grid[i][j])
                    if dp[i][j-1][kk-c] > -inf:
                        dp[i][j][kk] = max(dp[i][j][kk], dp[i][j-1][kk-c] + grid[i][j])
        ans = max(dp[m-1][n-1])
        return ans if ans > -inf else -1

# ping pong memory optimization
# dont forget to reset before computation
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-inf for _ in range(k+1)] for _ in range(n)] for _ in range(2)]
        dp[0][0][int(grid[0][0] > 0)] = grid[0][0]
        for j in range(1, n):
            c = int(grid[0][j] > 0)
            for kk in range(c, k+1):
                if dp[0][j-1][kk-c] > -inf:
                    dp[0][j][kk] = dp[0][j-1][kk-c] + grid[0][j]
        
        for i in range(1, m):
            for j in range(n):
                c = int(grid[i][j] > 0)
                dp[i%2][j][0] = -inf
                for kk in range(c, k+1):
                    dp[i%2][j][kk] = -inf
                    if j == 0:
                        if dp[1-i%2][0][kk-c] > -inf:
                            dp[i%2][0][kk] = dp[1-i%2][0][kk-c] + grid[i][0]
                        continue
                    if dp[1-i%2][j][kk-c] > -inf:
                        dp[i%2][j][kk] = max(dp[i%2][j][kk], dp[1-i%2][j][kk-c] + grid[i][j])
                    if dp[i%2][j-1][kk-c] > -inf:
                        dp[i%2][j][kk] = max(dp[i%2][j][kk], dp[i%2][j-1][kk-c] + grid[i][j])
        ans = max(dp[(m-1)%2][n-1])
        return ans if ans > -inf else -1