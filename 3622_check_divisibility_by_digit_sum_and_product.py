# easy
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, p, k = 0, 1, n
        while k:
            d = k % 10
            s += d
            p *= d
            k //= 10
        return n % (s + p) == 0