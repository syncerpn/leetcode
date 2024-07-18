# easy
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums) // 2):
            nums[2*i], nums[2*i+1] = nums[2*i+1], nums[2*i]
        return nums