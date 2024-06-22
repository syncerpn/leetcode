# alternating bits means that if xor with its >> 1 results in all 1
# and then + 1 will result in power-of-2
# so, simply calculate the result and check if it is power-of-2
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        k = n ^ (n >> 1)
        return k & (k + 1) == 0