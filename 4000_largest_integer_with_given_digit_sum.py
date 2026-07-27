# easy
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        a = 0
        while n > 0:
            if s >= 9:
                a = a * 10 + 9
                s -= 9
            else:
                a = a * 10 + s
                s -= s
            n -= 1
        
        return a if s == 0 else -1