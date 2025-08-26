# along the line
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = [0] * (m * n)
        flip, idx = False, 0
        for d in range(m+n-1):
            if flip == 0:
                i = min(d, m-1)
                j = d - i
                while i >= 0 and j < n:
                    ans[idx] = mat[i][j]
                    i -= 1
                    j += 1
                    idx += 1
            else:
                j = min(d, n-1)
                i = d - j
                while j >= 0 and i < m:
                    ans[idx] = mat[i][j]
                    i += 1
                    j -= 1
                    idx += 1
            flip = not flip
        return ans