# not other but dijkstra lol
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        h = [(-health + grid[0][0], (0, 0))]
        v = set([(i, j) for j in range(n) for i in range(m)])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while h:
            hp, pos = heapq.heappop(h)
            i, j = pos
            if i == m-1 and j == n-1:
                return hp < 0
            if (i, j) not in v:
                continue
            v.discard((i, j))
            for di, dj in d:
                if (i + di, j + dj) in v:
                    heapq.heappush(h, (hp + grid[i+di][j+dj], (i+di, j+dj)))