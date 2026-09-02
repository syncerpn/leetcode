# fairly easy with fast pow trick (sqrt)
class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7

        @functools.cache
        def fast_pow(k, p):
            if p == 1:
                return k % MOD
            if p == 0:
                return 1

            m = fast_pow(k, p // 2)
            if p % 2:
                return (m * m * k) % MOD
            else:
                return (m * m) % MOD
        
        ans = 0
        for a in nums:
            w = a % 10
            d = a // 10
            m = 1
            t = 10 ** w
            while d // m >= t:
                m *= 10
            
            k = d // m
            p = d % m
            ans += fast_pow(k, p)
        return ans % MOD