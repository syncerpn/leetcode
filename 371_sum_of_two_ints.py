# must solve without +/-
# then you have to implement adder
# complete solution with overflow checking and shits
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        mask = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        if (a >> 31) & 1:
            return ~(a ^ mask)
        return a