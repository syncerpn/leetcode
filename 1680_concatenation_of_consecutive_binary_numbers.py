# tracking number of bits
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        t = 2
        k = 1
        p = 0
        for a in range(1, n+1):
            if a >= t:
                t <<= 1
                k += 1
            p = (p << k) | a
            p %= MOD
        return p