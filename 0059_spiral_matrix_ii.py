# spiral traversal
# turn when next cell is not a valid cell or empty cell
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        ans[0][0] = 1
        d = [(0,1), (1,0), (0,-1), (-1,0)]

        t = 0
        x, y = d[t]
        i, j = 0, 0
        k = 2
        while k <= n * n:
            while i+x < 0 or i+x >= n or j+y < 0 or j+y >= n or ans[i+x][j+y] > 0:
                t = (t + 1) % 4
                x, y = d[t]

            i += x
            j += y
            ans[i][j] = k
            k += 1
        return ans