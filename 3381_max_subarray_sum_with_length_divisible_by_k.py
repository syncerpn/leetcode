# dp + prefix sum
# track min prefix sum with mod-k length
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        dp = [float("inf")] * k
        dp[0] = 0
        s = 0
        ans = -float("inf")

        for i, a in enumerate(nums):
            s += a
            j = (i + 1) % k
            if dp[j] != float("inf"):
                ans = max(ans, s - dp[j])
            dp[j] = min(s, dp[j])
        return ans

# same idea, but faster runtime
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        dp = [float("inf")] * k
        dp[0] = 0
        s = 0
        ans = -float("inf")

        for i, a in enumerate(nums):
            s += a
            j = (i + 1) % k
            if s < dp[j]:
                if dp[j] != float("inf"):
                    ans = max(ans, s - dp[j])
                dp[j] = s
            else:
                ans = max(ans, s - dp[j])
        return ans