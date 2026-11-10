# dp memoi
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])

        @functools.cache
        def move(p, d):
            x, y = p
            a, b = d
            x += a
            y += b
            if x == m - 1 and y == n - 1:
                return 1
            if x < m and y < n:
                if grid[x][y] == 1:
                    return move((x, y), (b, a)) % MOD
                return (move((x, y), (a, b)) % MOD + move((x, y), (b, a)) % MOD) % MOD
            return 0

        return (move((0, 0), (0, 1)) + move((0, 0), (1, 0))) % MOD

# true dp
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_cur = [0] * n
        row_cur[0] = 1
        for row in grid:
            row_prev, row_cur, cell_prev = row_cur, [0] * n, 0
            
            for i, p in enumerate(row_prev):
                if row[i] == 0:
                    row_cur[i], cell_prev = cell_prev + p, cell_prev + p
                else:
                    row_cur[i], cell_prev = cell_prev, p

        return row_cur[-1] %1_000_000_007