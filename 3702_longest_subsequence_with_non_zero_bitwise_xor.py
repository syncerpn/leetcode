# be aware of all 0s
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        z = 0
        for a in nums:
            if a == 0:
                z += 1
            else:
                ans ^= a
        if ans != 0:
            return n
        if z == n:
            return 0
        return n - 1
        