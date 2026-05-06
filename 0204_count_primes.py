# prime filter
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        P = [True] * n
        P[0] = False
        P[1] = False
        for a in range(2, int(n**0.5) + 1):
            if not P[a]:
                continue
            b = a * a
            while b < n:
                P[b] = False
                b += a
        return sum(P)