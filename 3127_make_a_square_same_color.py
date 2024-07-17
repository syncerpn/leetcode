# a bit tedious with mat sliding window
# seems like everyday stuff with mat
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        grid = [[grid[i][j] == "B" for j in range(3)] for i in range(3)]
        s = [sum(grid[i][j:j+2]) + sum(grid[i+1][j:j+2]) for j in range(2) for i in range(2)]
        for si in s:
            if si != 2:
                return True
        return False