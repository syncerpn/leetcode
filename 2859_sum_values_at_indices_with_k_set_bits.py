# bit count
# maybe use dp and memoi to make it O(n)
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def bit_sum(n):
            s = 0
            while n:
                s += n & 1
                n >>= 1
            return s
        
        c = 0
        for i, n in enumerate(nums):
            c += n if bit_sum(i) == k else 0
        return c