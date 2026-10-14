# easy
class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        for i, a in enumerate(nums):
            if i < n // 2:
                l += a
            else:
                r += a
        ans = int(l > r)
        for i in range(n-1):
            l = l - nums[i] + nums[(i + n // 2) % n]
            r = r + nums[i] - nums[(i + n // 2) % n]
            if l > r:
                ans += 1
        return ans