# easy
class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        for i in range(n):
            k = rowShift[i]
            grid[i] = grid[i][k:] + grid[i][:k]

        grid = list(zip(*grid))
        for i in range(n):
            k = colShift[i]
            grid[i] = grid[i][k:] + grid[i][:k]
        return list(zip(*grid))