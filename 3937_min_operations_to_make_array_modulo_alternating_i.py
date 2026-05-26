# brute-force
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(2)]
        for i, a in enumerate(nums):
            ii = i % 2
            m = a % k
            for j in range(m):
                dp[ii][j] += min(m - j, j + k - m)
            
            for j in range(m, k):
                dp[ii][j] += min(j - m, m - j + k)
        
        ans = inf
        for i in range(k):
            for j in range(k):
                if i == j:
                    continue
                ans = min(ans, dp[0][i] + dp[1][j])
        return ans