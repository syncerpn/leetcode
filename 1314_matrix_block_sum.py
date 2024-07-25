# row sum then col sum using prefix sum
# need to reshape at the end
# with zip, of course
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row_sums = []
        m = len(mat)
        n = len(mat[0])
        for row in mat:
            rsi = [sum(row[:k+1])]
            for i in range(1, n):
                s = rsi[-1]
                if i-k-1 >= 0:
                    s -= row[i-k-1]
                if i+k < n:
                    s += row[i+k]
                rsi.append(s)
            row_sums.append(rsi)
        
        ans = []
        mat = zip(*row_sums)
        for i, col in enumerate(mat):
            csi = [sum(col[:k+1])]
            for j in range(1, m):
                s = csi[-1]
                if j-k-1 >= 0:
                    s -= col[j-k-1]
                if j+k < m:
                    s += col[j+k]
                csi.append(s)
            ans.append(csi)
        
        return zip(*ans)