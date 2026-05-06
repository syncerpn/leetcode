# easy
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n == 3:
                n = 1
                ans += 1
            elif n % 2 == 0:
                n >>= 1
            elif n % 4 == 1:
                n -= 1
            else:
                n += 1
            ans += 1
        return ans