# easy
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_one = [sum(g) for g in grid]
        col_one = [sum(g) for g in zip(*grid)]
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (row_one[i] + col_one[j]) - (m + n)
        return grid