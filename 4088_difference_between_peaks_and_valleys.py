# easy
class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        p, v = 0, 0
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                p += nums[i]
            elif nums[i] < nums[i+1] and nums[i] < nums[i-1]:
                v += nums[i]
        return p - v