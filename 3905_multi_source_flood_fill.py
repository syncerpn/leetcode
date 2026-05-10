# sort so that we visit each cell once
class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        sources.sort(key=lambda s: -s[2])
        A = [[0] * m for _ in range(n)]
        for i, j, c in sources:
            A[i][j] = c
        
        for i, j, c in sources:
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and A[x][y] == 0:
                    A[x][y] = c
                    sources.append([x, y, c])
        return A