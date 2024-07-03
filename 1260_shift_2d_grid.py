# flatten, shift, then reform
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m*n)
        grid = sum(grid, [])
        grid = grid[-k:] + grid[:-k]
        return [[grid[i*n+j] for j in range(n)] for i in range(m)]