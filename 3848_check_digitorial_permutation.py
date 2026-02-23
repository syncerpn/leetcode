# easy
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        F = [1]
        s = 0
        k = n
        while k > 0:
            d = k % 10
            k //= 10
            while d >= len(F):
                F.append(F[-1] * len(F))
            s += F[d]

        return sorted(str(s)) == sorted(str(n))