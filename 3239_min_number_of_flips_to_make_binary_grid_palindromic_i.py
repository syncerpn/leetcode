# check row and col, then take the min
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r = sum(sum(grid[i][j] != grid[i][-1-j] for i in range(m)) for j in range(n//2))
        c = sum(sum(grid[i][j] != grid[-1-i][j] for i in range(m//2)) for j in range(n))
        return min(r, c)