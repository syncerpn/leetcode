# pairwise check
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        for a, b in pairwise(nums):
            if (a & 1) == (b & 1):
                return False
        return True