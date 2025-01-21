# it is easy to come up and optimize with prefix sum
# but the early stopping condition is just beautiful
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        p = sum(grid[0]) - grid[0][0]
        q = 0
        ans = max(p, q)
        for j in range(1, n):
            p -= grid[0][j]
            q += grid[1][j-1]
            m = max(p, q)
            if ans < m: # the early stopping condition which bases on math; beautiful
                break
            ans = m
        return ans