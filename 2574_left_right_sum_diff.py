# prefix sum, in-place beauty
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        r = sum(nums)
        l = 0
        for i in range(len(nums)):
            l, r = l + nums[i], r - nums[i]
            nums[i] = abs(r - l + nums[i])
        
        return nums