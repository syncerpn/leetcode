# recursive solution
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 1
        while i < n:
            i *= 4
        return i == n

#1. bitwise solution is just beautiful
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n > 0) and (n & (n - 1) == 0) and (n & 0x55555555 != 0)