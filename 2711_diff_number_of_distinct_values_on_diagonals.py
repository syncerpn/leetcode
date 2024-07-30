# fucking annoying indexing
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            l = Counter()
            r = Counter([grid[i+j][j] for j in range(1, min(n, m-i))])
            ans[i][0] = len(r)
            for j in range(1, min(n, m-i)):
                gl = grid[i+j-1][j-1]
                gr = grid[i+j][j]
                r[gr] -= 1
                if r[gr] == 0:
                    del r[gr]
                l[gl] += 1
                ans[i+j][j] = abs(len(r)-len(l))

        for j in range(1,n):
            l = Counter()
            r = Counter([grid[i][i+j] for i in range(1, min(m, n-j))])
            ans[0][j] = len(r)
            for i in range(1, min(m, n-j)):
                gl = grid[i-1][i+j-1]
                gr = grid[i][i+j]
                r[gr] -= 1
                if r[gr] == 0:
                    del r[gr]
                l[gl] += 1
                ans[i][i+j] = abs(len(r)-len(l))
        return ans