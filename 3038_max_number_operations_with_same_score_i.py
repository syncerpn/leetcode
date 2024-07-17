# easy
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        c = 1
        s = nums[0] + nums[1]
        i = 2
        while i < len(nums) - 1:
            if nums[i] + nums[i+1] != s:
                break
            c += 1
            i += 2
        return c
