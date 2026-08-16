# classic sliding window
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        d = Counter()
        ans = 0
        for r in range(n):
            a = nums[r]
            d[a] += 1
            while d[a] > k:
                b = nums[l]
                d[b] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans