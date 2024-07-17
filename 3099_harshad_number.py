# use string conversion for clean code
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum([int(c) for c in str(x)])
        return s if x % s == 0 else -1