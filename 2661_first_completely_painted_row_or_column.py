# hash map
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        r = [0] * m
        c = [0] * n
        d = {}
        for i, row in enumerate(mat):
            for j, a in enumerate(row):
                d[a] = (i, j)
        
        for k, a in enumerate(arr):
            i, j = d[a]
            r[i] += 1
            c[j] += 1
            if r[i] == n or c[j] == m:
                return k
        
        return m * n - 1