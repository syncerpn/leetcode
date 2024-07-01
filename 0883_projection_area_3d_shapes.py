# projection height equals to max height of towers in the same dimension
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy = sum([sum([c > 0 for c in grid[i]]) for i in range(n)])
        xz = sum([max(r) for r in grid])
        yz = sum([max([grid[i][j] for i in range(n)]) for j in range(n)])
        return xy + xz + yz