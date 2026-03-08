# easy
class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        p = 1
        s = sum(nums)
        for i in range(n-1, -1, -1):
            s -= nums[i]
            if p == s:
                return i
            if p > s:
                break
            p *= nums[i]
        return -1