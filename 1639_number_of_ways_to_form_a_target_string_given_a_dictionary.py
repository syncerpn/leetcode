# recursive + memoi + early stopping (to pass, lol)
# i felt like it could be solved with dp
# just kinda like common sequence
# but ended up with this solution because this was easier to implement
# anyway, im happy because i solved a hard question today
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        ans = [0]
        d = [collections.Counter(l) for l in zip(*words)]
        m, n = len(target), len(d)

        @functools.cache
        def forming(i, j):
            if i >= m:
                return 1
            if j >= n:
                return 0
            w = 0
            for k in range(j, n):
                if target[i] in d[k]:
                    wi = forming(i+1, k+1)
                    if wi == 0:
                        break
                    w += d[k][target[i]] * wi
            return w

        ans = forming(0, 0)
        return ans % (10 ** 9 + 7)

# and yes, i was right
# it can be solved with simple dp
# idea by lee215
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(target), len(words[0])

        dp = [1] + [0] * m
        for i in range(n):
            d = collections.Counter(w[i] for w in words)
            for j in range(m-1, -1, -1):
                dp[j+1] += dp[j] * d[target[j]] % MOD
        return dp[m] % MOD