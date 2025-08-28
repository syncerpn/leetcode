# easy
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            s = []
            x, y = i, 0
            while x < n and y < n:
                s.append(grid[x][y])
                x += 1
                y += 1
            s.sort()
        
            x, y = i, 0
            while x < n and y < n:
                ans[x][y] = s.pop()
                x += 1
                y += 1

        for j in range(1, n):
            s = []
            x, y = 0, j
            while x < n and y < n:
                s.append(grid[x][y])
                x += 1
                y += 1
            s.sort(reverse=True)
        
            x, y = 0, j
            while x < n and y < n:
                ans[x][y] = s.pop()
                x += 1
                y += 1

        return ans
