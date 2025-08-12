# as knapsack
# tried 1d dp but not work
# have to use 2d dp
# where dp[i][j] = the way to form a sum of j from the first i distinct integers
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            ix = i ** x
            for j in range(n+1):
                dp[i][j] = dp[i-1][j]
                if j >= ix:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-ix]) % MOD
        return dp[n][n]

# good 1d dp
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        ps = []
        i = 1
        while True:
            p = pow(i, x)
            if p > n:
                break
            ps.append(p)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1
        for p in ps:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]