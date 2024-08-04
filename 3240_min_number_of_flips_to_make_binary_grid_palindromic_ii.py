# row and col are both palindromic
# this condition is not a big deal
# we only need to care about the middle row or col or both
# for the count of ones to be divisible by 4
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m//2):
            for j in range(n//2):
                s = grid[i][j] + grid[i][-1-j] + grid[-1-i][j] + grid[-1-i][-1-j]
                ans += min(s, 4 - s)
        
        ones = 0 # for edge cases of the middle row/col/both
        odds = 0
        if m % 2 == 1:
            for j in range(n//2):
                if grid[m//2][j] != grid[m//2][-1-j]:
                    ans += 1
                    odds += 1
                else:
                    if grid[m//2][j] == 1:
                        ones += 2
        if n % 2 == 1:
            for i in range(m//2):
                if grid[i][n//2] != grid[-1-i][n//2]:
                    ans += 1
                    odds += 1
                else:
                    if grid[i][n//2] == 1:
                        ones += 2
        if m % 2 == 1 and n % 2 == 1:
                ans += grid[m//2][n//2] != 0
        
        if ones % 4 != 0:
            if odds == 0:
                ans += 2
                
        return ans