#1. linear search might be trivial, but binary search is more optimized
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        while l <= r:
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
        return m + 1