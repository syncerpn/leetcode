# simply pairwise difference
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for a, b in pairwise(nums):
            if b < a:
                ans += a - b
        return ans