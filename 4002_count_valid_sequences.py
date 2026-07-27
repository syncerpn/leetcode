# math method
# stars and bars algorithm and math
class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        ans = math.comb(n-1, k-1) % MOD
        odd = 0
        if n % 2 == k % 2:
            odd = math.comb((n-k) // 2 + k - 1, k - 1) % MOD
        return (ans - odd) % MOD

# above, but use own implementation of combination function
class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        def nCr(n ,r):
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n // 2:
                r = n - r
            num = 1
            den = 1
            for i in range(1, r + 1):
                num = (num * (n - i + 1)) % MOD
                den = (den * i) % MOD
            return (num * pow(den, MOD - 2, MOD)) % MOD

        ans = nCr(n-1, k-1) % MOD
        odd = 0
        if n % 2 == k % 2:
            odd = nCr((n-k) // 2 + k - 1, k - 1) % MOD
        return (ans - odd) % MOD