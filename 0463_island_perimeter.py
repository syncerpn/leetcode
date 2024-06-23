# each land gives 4
# common sides should be removed
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        common_sides = 0
        lands = 0
        row = len(grid)
        col = len(grid[0])
        for ri in range(row):
            for ci in range(col):
                if grid[ri][ci]:
                    lands += 1
                    if ri <= row - 2:
                        common_sides += grid[ri+1][ci]
                    if ci <= col - 2:
                        common_sides += grid[ri][ci+1]
        
        p = lands * 4 - 2 * common_sides
        return p