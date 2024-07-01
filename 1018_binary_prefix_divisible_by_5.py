# inplace + bit manip
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        k = 0
        for i, n in enumerate(nums):
            k = (k << 1) | n
            nums[i] = k % 5 == 0
        return nums