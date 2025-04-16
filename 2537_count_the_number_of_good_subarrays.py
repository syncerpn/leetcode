# sliding window
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = 0
        l = 0
        d = {}
        ans = 0
        for r in range(n):
            a = nums[r]
            if a not in d:
                d[a] = 0
            m += d[a]
            d[a] += 1
            while m >= k:
                ans += n - r
                b = nums[l]
                d[b] -= 1
                m -= d[b]
                l += 1
        
        return ans