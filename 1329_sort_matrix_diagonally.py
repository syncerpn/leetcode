# padding solution
# after padding, we transform all diagonals into columns of the new mat
# then sort and reform
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        CONSTRAINT_MAX = 101
        CONSTRAINT_MIN = 0
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            mat[i] = [CONSTRAINT_MIN] * (m-1-i) + mat[i] + [CONSTRAINT_MAX] * i
        
        mat = [list(sorted(col)) for col in zip(*mat)]
        mat = [list(c) for c in zip(*mat)]
        
        for i in range(m):
            mat[i] = mat[i][m-1-i:m-1-i+n]
        
        return mat

# also well solvable with heapq