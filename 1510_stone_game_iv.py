# basic dp
dp = [False] * 100001
for i in range(100001):
    j = 1
    while not dp[i] and j * j <= i:
        dp[i] = dp[i] | (not dp[i - j * j])
        j += 1

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return dp[n]

# if not pre-computed
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]