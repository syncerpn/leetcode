# in the end, we may have zero or only one negative
# try to minimize that negative if any
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = abs(matrix[0][0])
        s = False
        ans = 0
        for row in matrix:
            for c in row:
                if c < 0:
                    s = not s
                m = min(m, abs(c))
                ans += abs(c)
        return ans if not s else ans - 2 * m