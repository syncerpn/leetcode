# easy
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        d, s = 0, 0
        while n > 0:
            a = n % 10
            d += a
            s += a * a
            n = (n - a) // 10
        return s - d >= 50