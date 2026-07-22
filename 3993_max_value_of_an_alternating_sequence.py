# looks easy
# but need to tune the formula quite a while
class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        return s + m * (n // 2) - ((n - 1) // 2) + int(n % 2)