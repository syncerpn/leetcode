# once dp is familiar, this becomes pretty straigth forward
# try to count number of operations to turn one column to 0, 1, ..., 9
# then the next column cost to change into 0, 1, ..., 9
# should be current cost + min of previous column different than 0, 1, ..., 9
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[m] * 10 for _ in range(n)]
        p = [0] * 10
        for j in range(n):
            d = Counter([grid[i][j] for i in range(m)])
            for i in range(10):
                dp[j][i] = m - d[i] + min(p[:i] + p[i+1:])
            p = dp[j]
        return min(dp[-1])