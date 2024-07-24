# convert then sort
# edge case n == 0 should be handled separately
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(n):
            if n == 0:
                return mapping[0]
            k = 1
            r = 0
            while n:
                r += k * mapping[n % 10]
                n //= 10
                k *= 10
            return r
        
        return sorted(nums, key=lambda n: convert(n))