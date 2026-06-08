# count it with and
class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        p = 0
        x = 1
        c = 0
        while x <= n:
            if (n & x) and p:
                c += 1
            p = n & x
            x <<= 1
        return c == 1