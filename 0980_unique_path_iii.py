# backtracking, again
# got it right in the first try, lol
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = [0]
        def find_path(p, d, v):
            i, j = p
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for q in neighbors:
                if q == d and len(v) == 0:
                    ans[0] += 1
                elif q in v:
                    v.discard(q)
                    find_path(q, d, v)
                    v.add(q)
        
        v = set()
        s = None
        d = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    v.add((i, j))
                elif grid[i][j] == 1:
                    s = (i, j)
                elif grid[i][j] == 2:
                    d = (i, j)
        
        find_path(s, d, v)
        return ans[0]