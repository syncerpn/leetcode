# the math is easy
# but looking at the constraint
# you need another layer of optimization
# lol, good problem
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        k = n // 2
        m = bin(k)[2:]
        b = 5 if n % 2 else 1
        
        ans = 1

        for i in m:
            ans = ans ** 2
            if i == "1":
                ans *= 20
            ans %= MOD
        
        return (ans * b) % MOD