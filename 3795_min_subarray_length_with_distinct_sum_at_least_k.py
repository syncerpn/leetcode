# sliding window
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        s = 0
        l = 0
        v = {}
        ans = float("inf")
        for r, a in enumerate(nums):
            if a not in v:
                v[a] = 0
            v[a] += 1
            if v[a] == 1:
                s += a
            while s >= k:
                ans = min(ans, r - l + 1)
                b = nums[l]
                v[b] -= 1
                if v[b] == 0:
                    s -= b
                l += 1
        
        return ans if ans < float("inf") else -1