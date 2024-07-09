# build diagonals and calculate sum
# remove duplication if any
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sp = sum([mat[i][i] for i in range(n)])
        ss = sum([mat[i][n-1-i] for i in range(n)])
        return sp + ss - mat[n//2][n//2] if n % 2 else sp + ss