# is this really a hard question, lol
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, n = 0, len(nums)
        p = 0
        ans = 0
        for r, a in enumerate(nums):
            p += a
            while p * (r - l + 1) >= k:
                p -= nums[l]
                l += 1
            
            ans += r - l + 1
        return ans