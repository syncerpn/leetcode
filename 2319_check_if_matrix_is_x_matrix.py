# check conditions
# we can also do it with two nested loop, checking every element
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        cond_diag = all([grid[i][i] for i in range(n)]) and all([grid[i][n-1-i] for i in range(n)])
        if not cond_diag:
            return False
        
        for i in range(n):
            grid[i][i] = 0
            grid[i][n-1-i] = 0
            if any(grid[i]):
                return False
        return True