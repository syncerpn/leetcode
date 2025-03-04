# easy
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        o, z = 0, 0
        for a in nums:
            if a % 2 == 0:
                z += 1
            else:
                o += 1
        return [0] * z + [1] * o