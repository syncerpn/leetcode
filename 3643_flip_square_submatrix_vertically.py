# easy
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for i in range(k//2):
            grid[x+i][y:y+k], grid[x+k-1-i][y:y+k] = grid[x+k-1-i][y:y+k], grid[x+i][y:y+k]
        return grid
                