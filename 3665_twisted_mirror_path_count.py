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