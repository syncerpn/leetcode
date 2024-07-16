# just check
class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        c = 0
        while n:
            d = n % 10
            if d and num % d == 0:
                c += 1
            n = n // 10
        return c