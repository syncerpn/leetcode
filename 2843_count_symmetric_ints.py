# just count each in range
# nothing special
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(n):
            if n >= 10 and n <= 99:
                return n // 10 == n % 10
            elif n >= 1000 and n <= 9999:
                l = n % 100
                h = n // 100
                return l // 10 + l % 10 == h // 10 + h % 10
            return False
        c = 0
        for i in range(low, high+1):
            c += is_symmetric(i)
        return c