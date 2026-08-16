# dp[i] = max score diff can be obtained from A[i:n]
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-inf] * (n + 1)
        dp[-1] = 0
        for i in range(n-1, -1, -1):
            t = 0
            for j in range(i, min(i+3, n)):
                t += stoneValue[j]
                dp[i] = max(dp[i], t - dp[j+1])
        return "Tie" if dp[0] == 0 else "Alice" if dp[0] > 0 else "Bob"

# space optimized version
# only need 4 dp slots
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4
        for i in range(n-1, -1, -1):
            t = 0
            dp[0] = -inf
            for k in range(min(3, n-i)):
                t += stoneValue[i+k]
                dp[0] = max(dp[0], t - dp[k+1])
            dp[1], dp[2], dp[3] = dp[0], dp[1], dp[2]
        return "Tie" if dp[0] == 0 else "Alice" if dp[0] > 0 else "Bob"

# still dp, but very good runtime
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        s1, s2, s3 = 0, 0, 0
        tot = 0

        for value in reversed(stoneValue):
            tot += value
            s1, s2, s3 = tot-min(s1,s2,s3), s1, s2
        bob = tot - s1
        if s1 > bob:
            return "Alice"
        if s1 < bob:
            return "Bob"
        return "Tie"