# dp, optimized to O(1) space
# kadane algorithm as well
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        a0 = -inf # ends with an added
        a1 = -inf # ends with a subtracted
        b0 = -inf # deletion used, ends with an added
        b1 = -inf # deletion used, ends with a subtracted
        ans = -inf
        for a in nums:
            b0, b1 = max(b1 + a, a0), max(b0 - a, a1)
            a0, a1 = max(a, a1 + a), a0 - a
            ans = max(ans, a0, a1, b0, b1)
        return ans