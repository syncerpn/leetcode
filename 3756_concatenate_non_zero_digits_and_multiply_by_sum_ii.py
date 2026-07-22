# prefix everything
# prefix sum of digits: p
# prefix concat of digits: x
# prefix count of non-zero digits: q
# for each query [l, r], we calculate:
# sum of digits within the range,
# concat num = concat digit prefix at r minus (concat digit prefix at l * modded power of 10)
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        MOD = 10**9 + 7
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD
        
        p = [0] * (n + 1)
        x = [0] * (n + 1)
        q = [0] * (n + 1)
        for i, c in enumerate(s):
            d = int(c)
            p[i + 1] = p[i] + d
            x[i + 1] = (x[i] * 10 + d) % MOD if d > 0 else x[i]
            q[i + 1] = q[i] + (d > 0)

        m = len(queries)
        ans = [0] * m
        for i in range(m):
            l = queries[i][0]
            r = queries[i][1] + 1
            length = q[r] - q[l]
            ans[i] = (x[r] - x[l] * pow10[length]) * (p[r] - p[l]) % MOD

        return ans