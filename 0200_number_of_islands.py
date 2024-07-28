# bfs, similar to #0695
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        v = set([(i, j) for j in range(n) for i in range(m) if grid[i][j] == "1"])
        
        ans = 0
        while v:
            ans += 1
            s = [v.pop()]
            while s:
                r, c = s.pop()
                for i, j in [(r+1, c), (r-1,c), (r, c+1), (r, c-1)]:
                    if 0 <= i < m and 0 <= j < n and (i, j) in v and grid[i][j] == "1":
                        s.append((i, j))
                        v.discard((i, j))
        return ans