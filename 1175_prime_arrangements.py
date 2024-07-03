# count arrangements of primes multiply with count arrangements of non-primes
# memoi + math
class Solution:
    _d = {}
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def factori(c):
            if c in Solution._d:
                return Solution._d[c]
            r = 1
            for i in range(1, c+1):
                r = (r * i) % MOD
            Solution._d[c] = r
            return r

        def is_prime(k):
            if k == 1:
                return False
            if k == 2:
                return True
            for i in range(2, int(k ** 0.5) + 1):
                if k % i == 0:
                    return False
            return True

        c = 0
        for i in range(n):
            k = i + 1
            if is_prime(k):
                c += 1
                
        return factori(c) * factori(n-c) % MOD