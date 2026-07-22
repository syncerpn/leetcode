# 2100 rated problem
# looked pretty scary at first
# then it is actually not that difficult
# solved with bfs to build the safeness map
# then simple dijkstra
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        s = [[inf] * n for _ in range(n)]
        h = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    heapq.heappush(h, (0, i, j))
                    s[i][j] = 0
        while h:
            c, i, j = heapq.heappop(h)
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ii = i + di
                jj = j + dj
                if 0 <= ii < n and 0 <= jj < n and s[ii][jj] == inf:
                    s[ii][jj] = -(c + 1)
                    heapq.heappush(h, (c + 1, ii, jj))

        v = [[False] * n for _ in range(n)]
        h = [(s[0][0], 0, 0)]
        v[0][0] = True
        while h:
            c, i, j = heapq.heappop(h)
            if i == n - 1 and j == n - 1:
                return -c
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ii = i + di
                jj = j + dj
                if 0 <= ii < n and 0 <= jj < n and not v[ii][jj]:
                    v[ii][jj] = True
                    heapq.heappush(h, (max(c, s[ii][jj]), ii, jj))
        return 0