# easy
# a xor b == 0 only when a == b
class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        ans = 0
        for a, b in pairwise(nums):
            if a == b:
                ans += 1
        return ans