# brilliant, division will not work
# flatten prefix product left and right
# for each element, multiply left of it and right of it
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        L, R = [], []
        l, r = 1, 1
        for i in range(m):
            for j in range(n):
                L.append(l)
                l = (l * grid[i][j]) % MOD
                R.append(r)
                r = (r * grid[~i][~j]) % MOD
        
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = (L[i*n+j] * R[~(i*n+j)]) % MOD
        return ans
        