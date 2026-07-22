# easy
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        return nums.count(nums[n//2]) == 1