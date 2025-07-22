# sliding window
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        p, ans = 0, 0
        l = 0
        for a in nums:
            while a in s:
                b = nums[l]
                p -= b
                s.remove(b)
                l += 1
            p += a
            ans = max(ans, p)
            s.add(a)
        return ans