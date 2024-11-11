# same as the previous easy version
# but with checking for the longest possible one
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 1
        p, q, n = 1, 1, len(nums)
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                q += 1
                ans = max(ans, max(min(p, q), q // 2))
            else:
                p, q = q, 1
        return ans
        