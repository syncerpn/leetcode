# dp
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dpn = [[ 1] * n for _ in range(m)]
        dpp = [[-1] * n for _ in range(m)]

        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dpn[0][0] = grid[0][0] if grid[0][0] <= 0 else  1
                    dpp[0][0] = grid[0][0] if grid[0][0] >= 0 else -1
                else:
                    if j > 0:
                        dpn[i][j] = min(dpn[i][j], dpn[i][j-1] * grid[i][j], dpp[i][j-1] * grid[i][j])
                        dpp[i][j] = max(dpp[i][j], dpn[i][j-1] * grid[i][j], dpp[i][j-1] * grid[i][j])
                    if i > 0:
                        dpn[i][j] = min(dpn[i][j], dpn[i-1][j] * grid[i][j], dpp[i-1][j] * grid[i][j])
                        dpp[i][j] = max(dpp[i][j], dpn[i-1][j] * grid[i][j], dpp[i-1][j] * grid[i][j])
        
        return dpp[m-1][n-1] % MOD if dpp[m-1][n-1] >= 0 else -1