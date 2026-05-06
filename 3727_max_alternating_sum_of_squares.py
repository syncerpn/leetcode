# easy
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(key=lambda x: abs(x))
        return sum(a * a * (int(i >= n//2) * 2 - 1) for i, a in enumerate(nums))