# short
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        return [grid[i][(1 - 2*(i%2))*j-(i%2)*(n%2)] for i in range(m) for j in range(n) if (i+j) % 2 == 0]