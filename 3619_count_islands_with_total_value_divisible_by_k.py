# bfs
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        v = set([(x, y) for y in range(n) for x in range(m) if grid[x][y] != 0])
        ans = 0
        while v:
            q = [v.pop()]
            s = 0
            while q:
                x, y = q.pop()
                s += grid[x][y]
                print(s)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    c = (x+dx, y+dy)
                    if (x+dx, y+dy) in v:
                        v.remove(c)
                        q.append(c)
            ans += s % k == 0
        return ans