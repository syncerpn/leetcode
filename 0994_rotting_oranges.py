# board walking bfs
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        s, v, ans, D = [], set(), 0, [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    v.add((i, j))
                elif grid[i][j] == 2:
                    s.append((i, j))
        
        while v:
            if not s:
                return -1
            s_next = []
            for i, j in s:
                for di, dj in D:
                    if (i+di, j+dj) in v:
                        s_next.append((i+di, j+dj))
                        v.discard((i+di, j+dj))
            s = s_next
            ans += 1
        
        return ans