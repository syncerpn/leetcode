# make use of the fact that the mat is sorted
# provide good early stopping
# O(m + n)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        c = 0
        p = 0
        for i in range(m-1, -1, -1):
            for j in range(p, n):
                if grid[i][j] < 0:
                    c += n - j
                    p = j
                    break
        return c