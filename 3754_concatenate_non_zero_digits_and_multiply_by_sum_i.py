# easy
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        s = [c for c in str(n) if c != "0"]
        return sum(list(map(int, s))) * int("".join(s))