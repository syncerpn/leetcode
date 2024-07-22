# try to flip all rows with leading 0
# then try to flip all cols with more 0 than 1
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                grid[i] = [1-k for k in grid[i]]
        
        colsum = [max(sum(g), m - sum(g)) for g in zip(*grid)]
        return sum([c << (n-1-i) for i, c in enumerate(colsum)])