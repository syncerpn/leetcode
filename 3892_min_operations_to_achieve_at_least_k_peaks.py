# got the idea
# but failed with the implementation
# so this is the help from others
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        def eval(nums, start, end, k, cost):
            n = len(nums)
            dp = [[inf] * (k + 1) for _ in range(n + 2)]
            dp[start][0] = 0
            for i in range(start, end + 1):
                for j in range(k + 1):
                    if dp[i][j] == inf:
                        continue
                    # skip current
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                    # take current
                    if j + 1 <= k:
                        dp[i + 2][j + 1] = min(dp[i + 2][j + 1], dp[i][j] + cost[i])
            return min(dp[end + 1][k], dp[end + 2][k])

        n = len(nums)
        if k > n // 2:
            return -1
        if k == 0:
            return 0
        if n == 2:
            return 1 if nums[0] == nums[1] else 0

        cost = [max(0, max(nums[i - 1], nums[(i + 1) % n]) + 1 - nums[i]) for i in range(n)]
        # case 1: skip index 0
        ans = eval(nums, 1, n - 1, k, cost)
        # case 2: take index 0
        if k >= 1:
            ans = min(ans, cost[0] + eval(nums, 2, n - 2, k - 1, cost))

        return ans