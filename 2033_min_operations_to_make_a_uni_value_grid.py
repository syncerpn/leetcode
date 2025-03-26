# sorting and median
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid = sorted([a for g in grid for a in g])
        n = len(grid)
        m = grid[n//2]
        ans = 0
        for a in grid:
            if a % x != m % x:
                return -1
            ans += abs(a - m) // x
        return ans

# the following solution is similar
# but using sum to append all list in the matrix
# is super slow
# took 7366ms (vs. 166ms in the above solution) is just crazy
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid = sorted(sum(grid, []))
        n = len(grid)
        m = grid[n//2]
        ans = 0
        for a in grid:
            if a % x != m % x:
                return -1
            ans += abs(a - m) // x
        return ans

# also someone suggested to use n-selection to make it O(n)