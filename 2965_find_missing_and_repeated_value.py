# use math
# find square diff and diff of the two target numbers
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid = sum(grid, [])
        n = len(grid)
        s = 0
        t = 0
        for i, n in enumerate(grid):
            s += n * n - (i + 1) * (i + 1)
            t += n - (i + 1)
        
        return [(s // t + t) // 2, (s // t - t) // 2]