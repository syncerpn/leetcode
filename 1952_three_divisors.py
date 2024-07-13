# such number should be square of a prime int
class Solution:
    def isThree(self, n: int) -> bool:
        def is_prime(k):
            if k == 1 or k == 2:
                return True
            q = int(k ** 0.5)
            if k % 2 == 0:
                return False
            for i in range(3, q+1):
                if k % i == 0:
                    return False
            return True

        if n == 1:
            return False
        s = int(n ** 0.5)
        return s * s == n and is_prime(s)