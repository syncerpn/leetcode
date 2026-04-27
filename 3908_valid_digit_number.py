# easy
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return str(n)[0] != str(x) and str(x) in str(n)[1:]