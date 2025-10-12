# easy
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 2
        p = 2
        n = len(nums)
        for i in range(2, n):
            if nums[i] == nums[i-1] + nums[i-2]:
                p += 1
                ans = max(ans, p)
            else:
                p = 2
        return ans