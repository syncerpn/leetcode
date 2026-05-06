# stupid edge case where grid[0][0] is not 0, lol
# other than that, easy
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        n = len(grid)
        f = [(0, 0)] * n * n
        for i, g in enumerate(grid):
            for j, a in enumerate(g):
                f[a] = (i, j)

        for (a, b), (c, d) in pairwise(f):
            if (abs(c - a) == 2 and abs(d - b) == 1) or (abs(c - a) == 1 and abs(d - b) == 2):
                continue
            return False
        return True