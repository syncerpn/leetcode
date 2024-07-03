# fairly easy
# it can be solved for general k moves
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        m = nums[-1] - nums[3]
        for i in range(3+1):
            d = nums[-1-i] - nums[3-i]
            if m > d:
                m = d
        return m