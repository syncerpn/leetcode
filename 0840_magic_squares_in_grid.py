# check and skip non-potentials
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        skipped = set()
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m-2):
            for j in range(n-2):
                if (i, j) in skipped:
                    continue
                cs = [-15,-15,-15]
                ds = [-15,-15]
                rs = [-15,-15,-15]
                v = set()
                for k in range(9):
                    r = k // 3
                    c = k  % 3
                    p = grid[i+r][j+c]
                    if p == 0 or p > 9:
                        skipped.add((i+r, j+c))
                        break
                    v.add(p)
                    rs[r] += p
                    cs[c] += p
                    if r == c:
                        ds[0] += p
                    if r + c == 2:
                        ds[1] += p
                else:
                    if len(v) != 9 or any(rs) or any(cs) or any(ds):
                        continue
                    ans += 1
                    skipped.add((i+1, j))
                    skipped.add((i, j+1))
                    skipped.add((i+1, j+1))
        return ans