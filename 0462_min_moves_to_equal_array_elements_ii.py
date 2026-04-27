# median, not mean
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = nums[n // 2]
        return sum(abs(a - m) for a in nums)