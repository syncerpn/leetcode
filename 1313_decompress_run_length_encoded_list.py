# python makes it easy
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        r = []
        for i in range(len(nums) // 2):
            f, v = nums[2*i], nums[2*i+1]
            r += [v] * f
        return r