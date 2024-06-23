# bit manip
class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        while n:
            i += n & 1
            n = n >> 1
        return i