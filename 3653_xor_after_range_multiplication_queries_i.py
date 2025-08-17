# simply brute-force thanks to the low constraints
# see #3655 for the harder version
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        for l, r, k, v in queries:
            while l <= r:
                nums[l] = (nums[l] * v) % MOD
                l += k
        ans = 0
        for a in nums:
            ans ^= a
        return ans