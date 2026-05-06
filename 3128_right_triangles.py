# a bit cumbersome
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        R = [[0] * n for _ in range(m)]
        C = [[0] * n for _ in range(m)]
        for i in range(m):
            s = sum(grid[i])
            for j in range(n):
                if grid[i][j] == 1:
                    R[i][j] = s
        
        for j in range(n):
            s = sum(grid[i][j] for i in range(m))
            for i in range(m):
                if grid[i][j] == 1:
                    C[i][j] = s
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += (R[i][j] - 1) * (C[i][j] - 1)
        return ans