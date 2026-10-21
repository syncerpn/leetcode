# brute force solution
class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            mi = ma = nums[i]
            for j in range(i+1, n):
                mi = min(mi, nums[j])
                ma = max(ma, nums[j])
                ans += ma - mi
        return ans