# recursive + memoi
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @functools.cache
        def extend(l, h):
            if h < 0:
                return 0
            return (l <= 0) + extend(l-zero, h-zero) % (10 ** 9 + 7) + extend(l-one, h-one) % (10 ** 9 + 7)
        
        ans = extend(low, high)
        return ans % (10 ** 9 + 7)

# a better dp solution
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] + [0] * high
        for i in range(high+1):
            if i >= zero:
                dp[i] += dp[i-zero]
            if i >= one:
                dp[i] += dp[i-one]
            dp[i] %= MOD
        
        return sum(dp[low:high+1]) % MOD
