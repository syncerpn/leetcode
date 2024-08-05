# not difficult
# but need to handle cases
# we divide one cell into top, left, right, bottom that take z = 0, 1, 2, 3 respectively
# then try to bfs the map to mark continuous regions
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid[0])
        s = set([(i, j, k) for i in range(n) for j in range(n) for k in range(4)])
        ans = 0
        while s:
            ans += 1
            q = [s.pop()]
            while q:
                q_next = []
                for x, y, z in q:
                    c = grid[x][y]
                    t, l, r, b = (x, y, 0), (x, y, 1), (x, y, 2), (x, y, 3)
                    u, d, p, a = (x-1, y, 3), (x+1, y, 0), (x, y-1, 2), (x, y+1, 1)
                    if c == "/" or c == " ":
                        if z == 0:
                            if l in s:
                                s.discard(l)
                                q_next.append(l)
                            if u in s:
                                s.discard(u)
                                q_next.append(u)
                        elif z == 1:
                            if t in s:
                                s.discard(t)
                                q_next.append(t)
                            if p in s:
                                s.discard(p)
                                q_next.append(p)
                        elif z == 2:
                            if b in s:
                                s.discard(b)
                                q_next.append(b)
                            if a in s:
                                s.discard(a)
                                q_next.append(a)
                        elif z == 3:
                            if r in s:
                                s.discard(r)
                                q_next.append(r)
                            if d in s:
                                s.discard(d)
                                q_next.append(d)

                    if c == "\\" or c == " ":
                        if z == 0:
                            if r in s:
                                s.discard(r)
                                q_next.append(r)
                            if u in s:
                                s.discard(u)
                                q_next.append(u)
                        elif z == 1:
                            if b in s:
                                s.discard(b)
                                q_next.append(b)
                            if p in s:
                                s.discard(p)
                                q_next.append(p)
                        elif z == 2:
                            if t in s:
                                s.discard(t)
                                q_next.append(t)
                            if a in s:
                                s.discard(a)
                                q_next.append(a)
                        elif z == 3:
                            if l in s:
                                s.discard(l)
                                q_next.append(l)
                            if d in s:
                                s.discard(d)
                                q_next.append(d)
                
                q = q_next
        return ans

# union-find solution shares the same idea
# but code looks much cleaner
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        f = {}
        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
        def union(x, y):
            f[find(x)] = find(y)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i - 1, j, 2), (i, j, 0))
                if j:
                    union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if grid[i][j] != "\\":
                    union((i, j, 3), (i, j, 0))
                    union((i, j, 1), (i, j, 2))
        return len(set(map(find, f)))