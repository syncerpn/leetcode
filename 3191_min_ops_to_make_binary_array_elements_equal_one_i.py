# greedily flip
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i], nums[i+1], nums[i+2] = 1, 1 - nums[i+1], 1 - nums[i+2]
                ans += 1
        return ans if nums[-2] == 1 and nums[-1] == 1 else -1