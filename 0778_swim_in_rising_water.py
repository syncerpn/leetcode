# simple dijkstra
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        v = set()
        h = [(grid[0][0], (0, 0))]
        while h:
            e, (x, y) = heapq.heappop(h)
            if x == n - 1 and y == n - 1:
                return e
            if (x, y) in v:
                continue
            v.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                xx = x + dx
                yy = y + dy
                if n - 1 >= xx >= 0 and n - 1 >= yy >= 0:
                    if (xx, yy) not in v:
                        heapq.heappush(h, (max(e, grid[xx][yy]), (xx, yy)))
        return -1