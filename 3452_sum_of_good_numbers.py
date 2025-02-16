# easy
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i, a in enumerate(nums):
            if i >= k and a <= nums[i-k]:
                continue
            if i <= n - 1 - k and a <= nums[i+k]:
                continue
            ans += a
        return ans