# two pass
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        r = {i: 0 for i in range(m)}
        c = {j: 0 for j in range(n)}
        for i in range(m):
            for j in range(n):
                ans += grid[i][j]
                r[i] += grid[i][j]
                c[j] += grid[i][j]

        for i in range(m):
            for j in range(n):
                if grid[i][j] and r[i] == 1 and c[j] == 1:
                    ans -= 1
        return ans

# also two pass
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r = [sum(g) for g in grid]
        c = [sum(g) for g in zip(*grid)]
        return sum(r[i] + c[j] > 2 for i in range(m) for j in range(n) if grid[i][j])