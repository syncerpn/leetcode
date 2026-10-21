# easy
class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        x, y = 0, 0
        n, m = len(grid), len(grid[0])
        d = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
        while True:
            dx, dy = d[grid[x][y]]
            grid[x][y] = 0
            xn = x + dx
            yn = y + dy
            if xn < 0 or xn >= n or yn < 0 or yn >= m or grid[xn][yn] == 0:
                break
            x, y = xn, yn
        return [x, y]