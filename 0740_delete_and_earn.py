# dp as usual
# like house robber that you cannot rob from neighbors
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = Counter(nums)
        n = max(nums)
        dp = [0] * (n + 1)
        if 1 in nums:
            dp[1] = nums[1]

        for i in range(2, n+1):
            s = 0 if i not in nums else nums[i] * i
            dp[i] = max(dp[i-1], dp[i-2] + s)

        return dp[n]