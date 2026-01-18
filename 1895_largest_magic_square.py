# prefix sum
# with early stopping condition for runtime optimization
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        R = [[0] * (n + 1) for _ in range(m)]
        C = [[0] * (m + 1) for _ in range(n)]

        for i in range(m):
            for j in range(n):
                R[i][j+1] = R[i][j] + grid[i][j]
                C[j][i+1] = C[j][i] + grid[i][j]
        
        def side_check(i, j, k):
            w = R[i][j+k] - R[i][j]
            h = C[j][i+k] - C[j][i]
            if h != w:
                return False
            f, b = grid[i][j], grid[i][j+k-1]

            for d in range(1, k):
                if w != R[i+d][j+k] - R[i+d][j]:
                    return False
                if h != C[j+d][i+k] - C[j+d][i]:
                    return False
                f += grid[i+d][j+d]
                b += grid[i+d][j+k-1-d]
            
            return f == b and f == h

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if side_check(i, j, k):
                        return k
        
        return 1