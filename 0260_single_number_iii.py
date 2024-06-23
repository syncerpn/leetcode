# calculate xor of all numbers; in the end, this equals xor of the two single numbers
# (with math proof) find a separator d equals and of the above result with its opposite
# the separator can divide the list into 2, and xor of two lists results in the two single numbers
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for n in nums:
            x ^= n
        
        d = x & -x

        a = 0
        b = 0
        for n in nums:
            if n & d == 0:
                a ^= n
            else:
                b ^= n
        
        return [a, b]