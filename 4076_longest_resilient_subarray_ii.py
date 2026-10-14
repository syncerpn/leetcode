# same as #4075
# all elements must have the same modulo
# length * modulo must have the same modulo
# fairly easy
class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        l = 0
        p = nums[0] % k
        n = len(nums)
        ans = 1
        for r in range(1, n):
            q = nums[r] % k
            while p != q:
                l += 1
                p = nums[l] % k
            if q == p and (r - l + 1) * p % k == p:
                ans = max(ans, r - l + 1)
        return ans