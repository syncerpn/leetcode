# easy
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        return sum(m - a for a in nums)