# easy
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        o = n * n
        e = (2 * n + 2) * n // 2
        return math.gcd(o, e)