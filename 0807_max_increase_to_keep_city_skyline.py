# keep row and col max
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(g) for g in grid]
        col_max = [max(g) for g in zip(*grid)]
        n = len(grid)
        s = 0
        for i in range(n):
            for j in range(n):
                s += min(row_max[i], col_max[j]) - grid[i][j]
        
        return s