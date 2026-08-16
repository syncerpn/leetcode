# math
class Solution:
    def kthDigit(self, k: int) -> int:
        f = 9
        n = 1
        k -= 1
        while k >= f * n:
            k -= f * n
            f *= 10
            n += 1
        d, r = 10 ** (n - 1) + k // n, k % n
        if r < n - 1 or d // 10 % 2 == 0:
            return int(str(d)[r])
        return 9 - int(str(d)[r])