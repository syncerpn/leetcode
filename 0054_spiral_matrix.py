# going spiraaaaaaaal
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        j = 0
        r, c = 0, -1
        ans = []
        while n:
            for i in range(n):
                r, c = r + d[j][0], c + d[j][1]
                ans.append(matrix[r][c])
            n, m = m-1, n
            j = (j + 1) % 4
        
        return ans