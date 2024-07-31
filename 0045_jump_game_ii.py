# practicing dp with O(n2)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            dp[i] = 1 + min(dp[i:i+nums[i]+1])
        return dp[0]

# bfs greedy
# trying to jump as far as possible
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        ans = 1
        l, r = 0, nums[0]
        while r < len(nums) - 1:
            l, r = r, max(i + nums[i] for i in range(l, r+1))
            ans += 1
        return ans