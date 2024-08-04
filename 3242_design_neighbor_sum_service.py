# easy
class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.g = grid
        self.d = {grid[i][j]: (i, j) for j in range(self.n) for i in range(self.n)}

    def adjacentSum(self, value: int) -> int:
        i, j = self.d[value]
        ans = 0
        if i - 1 >= 0:
            ans += self.g[i-1][j]
        if i + 1 < self.n:
            ans += self.g[i+1][j]
        if j - 1 >= 0:
            ans += self.g[i][j-1]
        if j + 1 < self.n:
            ans += self.g[i][j+1]
        return ans

    def diagonalSum(self, value: int) -> int:
        i, j = self.d[value]
        ans = 0
        if i - 1 >= 0 and j - 1 >= 0:
            ans += self.g[i-1][j-1]
        if i + 1 < self.n and j - 1 >= 0:
            ans += self.g[i+1][j-1]
        if i - 1 >= 0 and j + 1 < self.n:
            ans += self.g[i-1][j+1]
        if i + 1 < self.n and j + 1 < self.n:
            ans += self.g[i+1][j+1]
        return ans


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)