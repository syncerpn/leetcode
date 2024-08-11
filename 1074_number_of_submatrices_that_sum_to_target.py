# brute-force even with prefix-sum does not work
# need hash table for quick counting
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0

        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        
        for j1 in range(n):
            for j2 in range(j1, n):
                d = {0: 1}
                p = 0
                for i in range(m):
                    p += matrix[i][j2] - (matrix[i][j1-1] if j1 > 0 else 0)
                    if p - target in d:
                        ans += d[p - target]
                    if p not in d:
                        d[p] = 0
                    d[p] += 1

        return ans