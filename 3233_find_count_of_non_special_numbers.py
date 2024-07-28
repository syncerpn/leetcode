# special numbers are square of a prime numbers
# we just need find all those square numbers in range l to r
# simply by checking the range int from sqrt of l to sqrt of r
# it reduces the time complexity a lot
class Solution:
    PRIMES = set([2,3])
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(n):
            if n in Solution.PRIMES:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n ** 0.5)+1, 2):
                if n % i == 0:
                    return False
            Solution.PRIMES.add(n)
            return True

        ls = int(l ** 0.5)
        rs = int(r ** 0.5) + 1
        ans = r - l + 1
        for n in range(ls, rs):
            if is_prime(n) and l <= n * n <= r and n != 1:
                ans -= 1
        return ans