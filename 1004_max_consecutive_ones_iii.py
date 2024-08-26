# we use if k < 0 instead of while k < 0
# just because doing so, we keep the maximum length info in r itself
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            k -= 1 - nums[r]
            if k < 0:
                k += 1 - nums[l]
                l += 1
        return r - l + 1