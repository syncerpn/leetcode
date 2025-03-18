# bit count, but this is slow
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        mask = [0] * 32
        l = 0
        for r, a in enumerate(nums):
            for i in range(32):
                mask[i] += (a >> i) & 1
            if any(m > 1 for m in mask):
                b = nums[l]
                for i in range(32):
                    mask[i] -= (b >> i) & 1
                l += 1
        
        return r - l + 1

# how about using or and xor to track unique bit position
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        s = 0
        l = 0
        ans = 1
        for r, a in enumerate(nums):
            while s & a:
                b = nums[l]
                s ^= b
                l += 1
            s |= a
            ans = max(ans, r - l + 1)
        return ans