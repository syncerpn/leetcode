# try to encode them and count the number of each candidate
# this solution uses string
# maybe just use tuple instead to make it faster
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = {}
        ans = 0
        for m in matrix:
            if m[0] == 0:
                s = "".join(str(c) for c in m)
            else:
                s = "".join(str(1 - c) for c in m)
            if s not in d:
                d[s] = 0
            d[s] += 1
            if d[s] > ans:
                ans = d[s]
        return ans