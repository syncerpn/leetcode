# dp
# using max num constraint as well
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[-1] * 1024 for _ in range(m)] for _ in range(n)]

        def dfs(i, j, xori):
            if i >= n or j >= m:
                return float('inf')

            xori ^= grid[i][j]

            if i == n - 1 and j == m - 1:
                return xori

            if dp[i][j][xori] != -1:
                return dp[i][j][xori]

            right = dfs(i, j + 1, xori)
            down = dfs(i + 1, j, xori)

            dp[i][j][xori] = min(right, down)
            return dp[i][j][xori]

        return dfs(0, 0, 0)
        