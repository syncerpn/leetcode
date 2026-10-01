# fairly easy
# run a lot faster with several conditions check
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        p = m + n - 1
        if p % 2 == 1 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        grid = [[1 if c == "(" else -1 for c in g] for g in grid]
        v = [[False] * n for _ in range(m)]
        @functools.cache
        def move(r, c, v):
            v += grid[r][c]
            if r == m - 1 and c == n - 1:
                return v == 0
            if 0 <= v <= p - (r + c + 1):
                if r < m - 1 and move(r + 1, c, v):
                    return True
                if c < n - 1 and move(r, c + 1, v):
                    return True
            return False
        return move(0, 0, 0)