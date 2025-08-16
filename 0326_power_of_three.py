# simple check
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 1
        while i < n:
            i *= 3
        
        return i == n

# one-trick
# must the largest power of 3 modulo n == 0
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0