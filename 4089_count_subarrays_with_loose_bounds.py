# easy
class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        ans = 0
        l = 0
        mi, ma = inf, -inf
        for i in range(len(nums)):
            mi = min(mi, nums[i])
            ma = max(ma, nums[i])
            if mi >= minK and ma <= maxK:
                ans += i - l + 1
            else:
                l = i + 1
                mi, ma = inf, -inf
        return ans