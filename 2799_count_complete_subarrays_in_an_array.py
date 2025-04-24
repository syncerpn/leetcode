# classic sliding windows
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s, n = len(set(nums)), len(nums)
        d = {}
        l = 0
        ans = 0
        for r in range(n):
            a = nums[r]
            if a not in d:
                d[a] = 0
            d[a] += 1
            while len(d) == s:
                ans += n - r
                b = nums[l]
                d[b] -= 1
                if d[b] == 0:
                    del d[b]
                l += 1
        return ans