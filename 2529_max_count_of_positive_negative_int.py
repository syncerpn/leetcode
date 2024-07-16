# array is sorted, so binary search is the way
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = bisect_left(nums, 0)
        r = bisect_right(nums, 0)
        return max(len(nums) - r, l)