# adjacent check
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        a = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h == 0:
                    continue
                a += 2 + 4 * h
                if j < n - 1:
                    tr = grid[i][j + 1]
                    a -= 2 * min(h, tr)
                if i < n - 1:
                    td = grid[i + 1][j]
                    a -= 2 * min(h, td)
        
        return a