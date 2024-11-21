# O(m * n)
# propagating
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(m)]
        for x, y in guards + walls:
            dp[x][y] = 1
        
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for x, y in guards:
            for dx, dy in DIRS:
                cx, cy = x, y
                while 0 <= cx + dx < m and 0 <= cy + dy < n and dp[cx+dx][cy+dy] != 1:
                    dp[cx+dx][cy+dy] = 2
                    cx += dx
                    cy += dy
        
        return sum(1 for i in range(m) for j in range(n) if dp[i][j] == 0)
