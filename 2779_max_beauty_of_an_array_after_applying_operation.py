# max overlaping interval
# O(n) time and space
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        d = [0] * (r - l + 2)
        for a in nums:
            m, n = max(l, a-k), min(r, a+k)
            d[m-l] += 1
            d[n-l+1] -= 1
        ans = 0
        t = 0
        for i in d:
            t += i
            ans = max(ans, t)
        return ans