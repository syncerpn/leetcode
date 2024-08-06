# sliding window with at most one zero
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        z = []
        m = 0
        n = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                n += 1
            else:
                if z:
                    n -= z[0] - l
                    l = z[0] + 1
                z = [r]
            m = max(m, n - (1 - len(z)))
        return m