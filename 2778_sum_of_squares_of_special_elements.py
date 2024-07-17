# lol the description again
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum([n * n for i, n in enumerate(nums) if len(nums) % (i+1) == 0])