# xor and bit count
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        n = 0
        while x:
            n += x & 1
            x >>= 1
        return n