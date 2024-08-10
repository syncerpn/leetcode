# backtracking
# with several early terminations
# 1. terminate when board has no 0-gold cells
# 2. terminate when the path being explored yield gold == total available gold
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = [0, sum([sum(gi) for gi in grid])]
        
        
        def explore(p, g):
            i, j = p
            g += grid[i][j]
            v[i][j] = True
            ans[0] = max(ans[0], g)
            if ans[0] == ans[1]:
                return True

            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and not v[x][y]:
                    if explore((x, y), g):
                        return True
            
            v[i][j] = False
            return False

        v = [[False if grid[i][j] > 0 else True for j in range(n)] for i in range(m)]
        if not any([any(vi) for vi in v]):
            return ans[1]

        for i in range(m):
            for j in range(n):
                if not v[i][j]:
                    if explore((i, j), 0):
                        return ans[1]

        return ans[0]