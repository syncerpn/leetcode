# dont need to sort, which i tried at first
# we can simply walk through pair of row and col sums from the beginning (0, 0)
# try to assign the min of the two to the current position
# and move to the next col/row of the min of the two
# while updating the larger one
# may also move to the next row/col if the larger one after updating is 0
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        mat = [[0 for _ in range(n)] for _ in range(m)]
        
        r = 0
        c = 0
        while r < m and c < n:
            if rowSum[r] < colSum[c]:
                mat[r][c] = rowSum[r]
                colSum[c] -= rowSum[r]
                r += 1
            else:
                mat[r][c] = colSum[c]
                rowSum[r] -= colSum[c]
                c += 1
                if rowSum[r] == 0:
                    r += 1
        return mat