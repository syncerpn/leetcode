# this may be a theory question
# any bit flip applied to any element of nums also flips the bit in array xor result
# therefore, we just need to check the bit diff between the array xor and k
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = k
        for n in nums:
            x ^= n
        
        r = 0
        while x:
            r += x & 1
            x >>= 1
        return r