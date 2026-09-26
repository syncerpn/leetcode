# needs revisit
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        def mod_pow(b, e):
            ans = 1
            while e > 0:
                if e & 1:
                    ans = ans * b % MOD
                b = b * b % MOD
                e >>= 1
            return ans
        
        N = n + k - 1
        R = 2 * k
        R = min(R, N - R)
        num = 1
        denum = 1

        for i in range(1, R + 1):
            num = num * (N - R + i) % MOD
            denum = denum * i % MOD
        
        idenum = mod_pow(denum, MOD - 2)
        return num * idenum % MOD