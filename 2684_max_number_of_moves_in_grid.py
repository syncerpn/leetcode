# dp is the best O(rc) time and O(r) space
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [True for _ in range(r)]
        ans = 0
        for j in range(1, c):
            dpn = []
            for i in range(r):
                m = dp[i] and (grid[i][j] > grid[i][j-1])
                if not m and i >= 1:
                    m = dp[i-1] and (grid[i][j] > grid[i-1][j-1])
                if not m and i <= r-2:
                    m = dp[i+1] and (grid[i][j] > grid[i+1][j-1])
                dpn.append(m)
                if m:
                    ans = j
            if not any(dpn):
                break
            dp = dpn
        return ans

# backtracking, even with early stopping did not pass