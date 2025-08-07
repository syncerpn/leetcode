# dp
# must check valid move for each child
# the child who starts at (0,0) has no other choice than moving in a perfect diagonal line
# the other childs may move n // 2 far away from the horizonal/vertical line from their starting positions to the destination
# so that they can end up at the destination
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        m = n - n // 2
        ans = 0
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0
        
        dp = [[0] * n for _ in range(n)]
        dp[0][-1] = fruits[0][-1]
        for i in range(1, n):
            if i < m:
                for j in range(n-i-1, n):
                    dp[i][j] = fruits[i][j] + max(dp[i-1][j-1:min(j+2, n)])
            else:
                for j in range(i, n):
                    dp[i][j] = fruits[i][j] + max(dp[i-1][j-1:min(j+2, n)])
        ans += dp[-1][-1]
        
        dp = [[0] * n for _ in range(n)]
        dp[0][-1] = fruits[-1][0]
        for i in range(1, n):
            if i < m:
                for j in range(n-i-1, n):
                    dp[i][j] = fruits[j][i] + max(dp[i-1][j-1:min(j+2, n)])
            else:
                for j in range(i, n):
                    dp[i][j] = fruits[j][i] + max(dp[i-1][j-1:min(j+2, n)])
        ans += dp[-1][-1]
        return ans