# bfs, similar to #0200
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        v = set([(i, j) for j in range(n) for i in range(m) if grid[i][j]])
        
        ans = 0
        while v:
            area = 0
            s = [v.pop()]
            while s:
                r, c = s.pop()
                area += 1
                for i, j in [(r+1, c), (r-1,c), (r, c+1), (r, c-1)]:
                    if 0 <= i < m and 0 <= j < n and (i, j) in v and grid[i][j]:
                        s.append((i, j))
                        v.discard((i, j))
            if area > ans:
                ans = area
        return ans