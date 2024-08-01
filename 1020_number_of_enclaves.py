# search only the edges
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        v = [[False] * n for _ in range(m)]
        for j in range(n):
            for i in [0, m-1]:
                if grid[i][j] == 0:
                    continue
                s = [(i, j)]
                while s:
                    x, y = s.pop()
                    if x < 0 or x >= m or y < 0 or y >= n or v[x][y] or grid[x][y] == 0:
                        continue
                    v[x][y] = True
                    s += [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

        for i in range(m):
            for j in [0, n-1]:
                if grid[i][j] == 0:
                    continue
                s = [(i, j)]
                while s:
                    x, y = s.pop()
                    if x < 0 or x >= m or y < 0 or y >= n or v[x][y] or grid[x][y] == 0:
                        continue
                    v[x][y] = True
                    s += [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        
        return sum(grid[i][j] for i in range(m) for j in range(n) if not v[i][j])