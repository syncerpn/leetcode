# bfs
# same as #0542
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        INF = float("inf")
        m, n = len(isWater), len(isWater[0])
        v = {(i, j) for j in range(n) for i in range(m)}
        h = [[INF] * n for _ in range(m)]
        s = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    h[i][j] = 0
                    s.append((i, j))
                    v.remove((i, j))
        while s:
            i, j = s.popleft()
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if (i+di, j+dj) not in v:
                    continue
                s.append((i+di, j+dj))
                v.remove((i+di, j+dj))
                h[i+di][j+dj] = min(h[i][j]+1, h[i+di][j+dj])
        return h