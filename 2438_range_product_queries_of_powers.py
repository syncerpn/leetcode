# fairly easy
# caching results to compute faster because of MOD
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        p = []
        i = 0
        while (1 << i) <= n:
            if n & (1 << i):
                p.append(i)
            i += 1
        q = list(accumulate(p, initial=0))
        ans = []
        
        @functools.cache
        def powmod(k):
            m = 1
            for _ in range(k):
                m = (m << 1) % MOD
            return m
        
        for l, r in queries:
            ans.append(powmod(q[r+1] - q[l]))
        return ans