# simple dp
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(0, n):
                matrix[i][j] += min(matrix[i-1][max(0,j-1):min(n,j+2)])
        
        return min(matrix[-1])