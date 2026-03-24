# easy
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        X, Y = [0] * n, [0] * n
        ans = 0
        for i in range(m):
            x, y = 0, 0
            for j in range(n):
                if grid[i][j] == "X":
                    x += 1
                elif grid[i][j] == "Y":
                    y += 1
                X[j] += x
                Y[j] += y
                if X[j] == Y[j] and X[j] > 0:
                    ans += 1
        
        return ans