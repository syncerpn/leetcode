# dp for a general value of k
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = {}
        ans = 0
        for a in nums:
            b = a % k
            if b not in dp:
                dp[b] = {b: 0}
            dp[b][b] += 1
            ans = max(ans, dp[b][b])

            for c in dp:
                if c == b:
                    continue
                if c not in dp[b]:
                    dp[b][c] = 1
                dp[c][b] = dp[b][c] + 1
                ans = max(ans, dp[c][b])
        return ans