# gcd, the sqrt check gcd for factors
# be aware of square gcd, which increases the factor count by only 1, while 2 for other cases
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a == 1 or b == 1:
            return 1

        while b:
            a, b = b, a % b
        
        c = 2
        k = int(a ** 0.5)
        if k * k == a:
            c -= 1

        for i in range(2, k+1):
            if a % i == 0:
                c += 2
        return c