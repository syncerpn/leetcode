# n & (n ^ x) wont change any 0-bit in original n into
# so the best achievable xor of the array is bitwise or of all numbers in the array
# because we will try to keep all 1-bit
# ----------
# 011 -> 001
# 010 -> 010
# 100 -> 100
# 110 -> 000
# -------xor
#        111
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        x = 0
        for n in nums:
            x |= n
        return x