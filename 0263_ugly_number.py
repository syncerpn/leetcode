# pure loop until reduced to 1, or else return False
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        ugly_factor = [2, 3, 5]
        for f in ugly_factor:
            while n % f == 0:
                n //= f
        
        return n == 1