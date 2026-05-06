# a bit of math
class Solution:
    def findNthDigit(self, n: int) -> int:
        p = 9
        q = 9
        i = 1
        while n > q:
            i += 1
            p *= 10
            q += p * i
        q -= p * i
        n -= q
        m = 10 ** (i - 1) + (n - 1) // i
        r = (n - 1) % i
        return int(str(m)[r])