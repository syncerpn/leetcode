# not that difficult with the given constraints
# could use sortedlist to implement
# but maybe just sort like this
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        p, q = m - k + 1, n - k + 1
        ans = [[0] * q for _ in range(p)]

        for i in range(p):
            for j in range(q):
                s = sorted(set(sum([grid[ii][j:j+k] for ii in range(i, i+k)], start=[])))
                if len(s) > 1:
                    ans[i][j] = min([abs(a-b) for a, b in pairwise(s)])
        
        return ans