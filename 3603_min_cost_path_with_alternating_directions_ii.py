# simple dp
class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        waitCost[m-1][n-1] = 0
        dp = [[float("inf")] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j])
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1])
                    dp[i][j] += (i + 1) * (j + 1) + waitCost[i][j]
        
        return dp[m-1][n-1]