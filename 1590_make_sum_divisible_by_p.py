# prefix sum O(n) should be okay
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums) % p
        if s == 0:
            return 0
        t, d = 0, {0: -1}
        ans = n = len(nums)
        for i, a in enumerate(nums):
            t = (t + a) % p
            q = (t - s) % p
            if q in d:
                ans = min(ans, i - d[q])
            d[t] = i
        return ans if ans != n else -1