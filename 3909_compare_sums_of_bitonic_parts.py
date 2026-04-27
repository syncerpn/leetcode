# easy
class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        d = 0
        for a, b in pairwise(nums):
            if b > a:
                d += a
            else:
                d -= b
        return -1 if d == 0 else (0 if d > 0 else 1)