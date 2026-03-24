# easy
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        dp = [0] * n
        for i in range(m):
            p = 0
            for j in range(n):
                p += grid[i][j]
                dp[j] += p
                if dp[j] > k:
                    break
                ans += 1
        return ans