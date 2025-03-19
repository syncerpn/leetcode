# simple dp
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
            ans = max(ans, matrix[i][0])

        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
            ans = max(ans, matrix[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]):
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                    ans = max(ans, matrix[i][j])
                else:
                    matrix[i][j] = 0
        
        return ans * ans