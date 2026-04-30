# easy math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        m = 5
        ans = 0
        while n >= m:
            ans += n // m
            m *= 5
        return ans