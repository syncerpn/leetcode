# pretty complicated though
class Solution:
    def completePrime(self, num: int) -> bool:
        @functools.cache
        def is_prime(a):
            if a == 0 or a == 1:
                return False
            if a == 2:
                return True
            if a % 2 == 0:
                return False
            for k in range(3, int(a ** 0.5) + 1, 2):
                if a % k == 0:
                    return False
            return True
        
        m = 10
        while num >= m:
            l = num // m
            r = num % m
            if not is_prime(l) or not is_prime(r):
                return False
            m *= 10
        return is_prime(num)