# editorial solution
# need revisited
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        res = float("inf")
        for _ in range(4):
            n, m = len(grid), len(grid[0])
            for i in range(1, n):
                a1 = self.minimumArea(grid[:i])
                for j in range(1, m):
                    part2 = [row[:j] for row in grid[i:]]
                    part3 = [row[j:] for row in grid[i:]]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    res = min(res, a1 + a2 + a3)
                for i2 in range(i + 1, n):
                    part2 = grid[i:i2]
                    part3 = grid[i2:]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    res = min(res, a1 + a2 + a3)
            grid = self.rotate(grid)
        return res

    def minimumArea(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        left, top, right, bottom = float("inf"), float("inf"), -1, -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    left = min(left, j)
                    top = min(top, i)
                    right = max(right, j)
                    bottom = max(bottom, i)
        if right == -1:
            return 0
        return (right - left + 1) * (bottom - top + 1)

    def rotate(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        return [[grid[i][j] for i in range(n-1, -1, -1)] for j in range(m)]
        