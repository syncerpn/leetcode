# easy
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        V = set((i, j) for i in range(m) for j in range(n) if grid[i][j] == 0)
        D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = 0
        while V:
            i, j = V.pop()
            S = [(i, j)]
            V.add((i, j))
            closed = True
            while S:
                i, j = S.pop()
                V.discard((i, j))
                for di, dj in D:
                    ii = i + di
                    jj = j + dj
                    if ii < 0 or ii >= m or jj < 0 or jj >= n:
                        closed = False
                        continue
                    if (ii, jj) in V:
                        S.append((ii, jj))
                        V.discard((ii, jj))
            if closed:
                ans += 1
        return ans
