# make a filter and do element-wise mult
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        w = [1,1,1,0,1,0,1,1,1]
        ans = 0
        for i in range(m-2):
            for j in range(n-2):
                f = sum([g[j:j+3] for g in grid[i:i+3]], [])
                s = sum([wi * fi for wi, fi in zip(w, f)])
                ans = max(ans, s)
        return ans