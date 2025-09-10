# initial solution
# dp probably
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        d, s = [0] * n, [0] * n
        d[0] = 1
        s[0] = 0
        for i in range(1, n):
            s[i] = s[i-1]
            if i >= delay:
                s[i] += d[i-delay]
            if i >= forget:
                s[i] -= d[i-forget]
            s[i] %= MOD
            d[i] = s[i]
        return (s[n-1] + sum(d[n-delay:n])) % MOD

# no need to track s
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        s = 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if i >= delay:
                s += dp[i-delay]
            if i >= forget:
                s -= dp[i-forget]
            s %= MOD
            dp[i] = s
        return (s + sum(dp[n-delay:n])) % MOD

# also possible to optimize memory O(forget)