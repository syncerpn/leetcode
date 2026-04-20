# easy
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = inf
        for a, b in pairwise(nums):
            ans = min(ans, b - a)
        return ans