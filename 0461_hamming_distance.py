# xor and bit count
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        count = 0
        while z:
            count += z & 1
            z = z >> 1
        
        return count