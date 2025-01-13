# with functools.cache and recursive dfs
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        @functools.cache
        def move(i, j, k):
            if i == m - 1 and j == n - 1:
                if coins[i][j] < 0 and k > 0:
                    return 0
                return coins[i][j]
            
            p = -float("inf")
            for x, y in [(0, 1), (1, 0)]:
                if i + x < m and j + y < n:
                    p = max(p, coins[i][j] + move(i + x, j + y, k))
                    if coins[i][j] < 0 and k > 0:
                        p = max(p, move(i + x, j + y, k - 1))
            return p
        return move(0, 0, 2)

# true dp
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        dp = [[[-float("inf")] * 3 for _ in range(n)] for _ in range(m)]

        dp[0][0][2] = 0
        dp[0][0][1] = 0
        dp[0][0][0] = coins[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for k in range(3):
                    g = coins[i][j]
                    if i > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + g)
                        if g < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                    if j > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + g)
                        if g < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
        return max(dp[m-1][n-1])