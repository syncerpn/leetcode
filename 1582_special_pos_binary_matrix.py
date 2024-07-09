# keep track of sum of each col and row
# then loop to test
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [sum(mat[i]) for i in range(m)]
        cols = [sum(p) for p in zip(*mat)]
        
        ans = 0
        for i in range(m):
            if rows[i] != 1:
                continue
            for j in range(n):
                if cols[j] != 1:
                    continue
                ans += mat[i][j]
        return ans