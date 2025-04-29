# sliding windows
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        m = max(nums)
        c = 0
        ans = 0
        for r, a in enumerate(nums):
            if a == m:
                c += 1
            while c >= k:
                ans += n - r
                if nums[l] == m:
                    c -= 1
                l += 1
        return ans