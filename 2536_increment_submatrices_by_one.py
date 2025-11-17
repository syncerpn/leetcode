# 1d line sweep, still works but slow
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        dp = [[0] * n for _ in range(n)]
        for rs, cs, re, ce in queries:
            for i in range(rs, min(n, re+1)):
                dp[i][cs] += 1
                if ce + 1 < n:
                    dp[i][ce + 1] -= 1
        for i in range(n):
            for j in range(1, n):
                dp[i][j] += dp[i][j-1]
        
        return dp

# 2d sweep, copied solution
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r2 + 1][c1] -= 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        
        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                above = mat[i - 1][j] if i > 0 else 0
                left = mat[i][j - 1] if j > 0 else 0
                diag = mat[i - 1][j - 1] if i > 0 and j > 0 else 0
                mat[i][j] = diff[i][j] + above + left - diag
        return mat