# kadane's algorithm again; just beautiful
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        d = nums[0]
        max_d = d
        for n in nums[1:]:
            d = max(d + n, n)
            if max_d < d:
                max_d = d
        return max_d