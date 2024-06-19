class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        r = len(grid)
        c = len(grid[0])
        # column condition
        if not all([len(set([grid[i][j] for i in range(r)])) == 1 for j in range(c)]):
            return False
        # row condition
        return all([a != b for a, b in pairwise(grid[0])])
        