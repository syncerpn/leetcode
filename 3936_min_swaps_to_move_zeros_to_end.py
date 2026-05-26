# easy
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        z = nums.count(0)
        n = len(nums)
        p = n - z
        ans = 0
        for i, a in enumerate(nums):
            if a == 0 and i < p:
                ans += 1
        return ans