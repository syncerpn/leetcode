# need revisit
# with fast mat mul
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        def mul(a, b):
            n = len(a)
            m = len(b[0])
            res = [[0] * m for _ in range(n)]

            for i in range(n):
                for k in range(len(a[0])):
                    r = a[i][k]
                    if r == 0:
                        continue
                    for j in range(m):
                        res[i][j] = (res[i][j] + r * b[k][j]) % MOD
            return res

        def powMul(base, exp, res):
            while exp > 0:
                if exp & 1:
                    res = mul(res, base)
                base = mul(base, base)
                exp >>= 1
            return res

        m = r - l + 1
        if n == 1:
            return m

        size = 2 * m
        u = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1
            for j in range(i + 1, m):
                u[i + m][j] = 1

        dp = [[1] * size]
        dp = powMul(u, n - 1, dp)
        ans = 0
        for i in range(size):
            ans = (ans + dp[0][i]) % MOD

        return ans