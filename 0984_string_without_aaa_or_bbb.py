# just a few cases
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if b >= a * 2: return "bba" * a + "b" * (b - a * 2)
        if b > a: return "bba" * (b - a) + "ba" * (a * 2 - b)
        if a >= b * 2: return "aab" * b + "a" * (a - b * 2)
        return "aab" * (a - b) + "ab" * (b * 2 - a)