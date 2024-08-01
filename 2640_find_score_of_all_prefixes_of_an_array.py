# prefix sum and prefix max
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        m, p = 0, 0
        for i, n in enumerate(nums):
            m = max(m, n)
            nums[i] += p + m
            p = nums[i]
        return nums