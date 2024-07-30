# simulate ball falling
# when it falls into one cell
# it should be drag left or right depending on the cell value is -1 or 1
# if the cell to which it is dragged is different from the one it just fell into
# it is trapped
# otherwise, keep falling to the next row until out of the grid
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(n):
            k = i
            j = 0
            while j < m:
                a = grid[j][k]
                if k + a < 0 or k + a >= n or grid[j][k+a] != a:
                    ans.append(-1)
                    break
                k += a
                j += 1
            else:
                ans.append(k)
        return ans