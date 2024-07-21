# xor to get bit difference
# and to get those 1 bit in k which cannot be made by changing n
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        x = n ^ k
        c = x & k
        if c:
            return -1
        s = 0
        while x:
            s += x & 1
            x >>= 1
        return s