# marked as hard
# but easier than the previous question in this contest
# simple dp by iterating all elements in nums
# check whether we should append it to the sequence
# the decision is made by checking whether the last two elements are one 1, two 1s, one 0, or two 0s
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        nums = [a & 1 for a in nums]
        dp = [[0] * 3 for _ in range(2)]
        for a in nums:
            b = 1 - a
            dp_next = [[0] * 3 for _ in range(2)]
            dp_next[a][2] = (dp[a][1] + dp[a][2]) % MOD
            dp_next[a][1] = (dp[a][1] + dp[b][1] + dp[b][2] + 1) % MOD
            dp_next[b][2] = dp[b][2] % MOD
            dp_next[b][1] = dp[b][1] % MOD
            dp = dp_next
        return (sum(dp[0]) % MOD + sum(dp[1]) % MOD) % MOD