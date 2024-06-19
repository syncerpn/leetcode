class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        
        # flatten mat
        f = []
        for a in mat:
            f += a
        
        # then simply return slices
        return [f[i*c:i*c+c] for i in range(m*n//c)]