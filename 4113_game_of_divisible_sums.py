# bottom up dp
class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        A = [0]
        n = len(nums)
        dp = [-inf] * (n + 1)
        dp[n] = 0
        
        for i in range(n-1, -1, -1):
            s = nums[i]
            if s % 3 == 0:
                dp[i] = max(dp[i], s - dp[i+1])
            else:
                dp[i] = max(dp[i], s + dp[i+1])
            if i < n - 1:
                s = nums[i] + nums[i+1]
                if s % 3 == 0:
                    dp[i] = max(dp[i], s - dp[i+2])
                else:
                    dp[i] = max(dp[i], s + dp[i+2])

        return dp[0]

# space optimized
class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n = len(nums)
        dp1, dp2 = nums[n-1], 0
        for i in range(n-2, -1, -1):
            a = nums[i]
            b = nums[i] + nums[i+1]
            dp1, dp2 = max((a + dp1) if a % 3 else (a - dp1), (b + dp2) if b % 3 else (b - dp2)), dp1

        return dp1