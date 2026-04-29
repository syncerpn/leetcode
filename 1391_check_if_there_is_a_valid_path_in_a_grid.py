# make it clean
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        L, R, T, B = {1, 4, 6}, {1, 3, 5}, {2, 3, 4}, {2, 5, 6}
        m, n = len(grid), len(grid[0])
        e = (m-1, n-1)
        grid = {(x, y): grid[x][y] for x in range(m) for y in range(n)}
        v = set([(x, y) for x in range(m) for y in range(n)])
        v.discard((0, 0))
        s = [(0, 0)]
        while s:
            c = s.pop()
            if c == e:
                return True
            x, y = c
            l, r, t, b = (x, y-1), (x, y+1), (x-1, y), (x+1, y)
            if grid[c] in R:
                if l in v and grid[l] in L:
                    s.append(l)
                    v.discard(l)
            if grid[c] in L:
                if r in v and grid[r] in R:
                    s.append(r)
                    v.discard(r)
            if grid[c] in B:
                if t in v and grid[t] in T:
                    s.append(t)
                    v.discard(t)
            if grid[c] in T:
                if b in v and grid[b] in B:
                    s.append(b)
                    v.discard(b)
        return False