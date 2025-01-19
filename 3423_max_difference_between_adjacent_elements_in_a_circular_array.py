# easy, and can be optimized to be O(1) space
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(a-b) for a, b in pairwise(nums + [nums[0]]))