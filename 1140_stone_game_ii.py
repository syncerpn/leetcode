# copied from lee
# so hard to understand
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n-2,-1,-1):
            piles[i] += piles[i + 1]
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n: return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return dp(0, 1)

# another, much better solution for understanding
# try to map it to a normal dp definition with states
# we will have
# dp(i, m, p) = best score for player p (Alice=True, Bob=False) choosing from index i of piles list and at most m piles
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        @functools.cache
        def dp(i, m, p):
            if i >= n:
                return 0
            s = -inf if p else inf
            si = 0
            for x in range(1, min(n - i, 2 * m) + 1):
                si += piles[i + x - 1]
                if p:
                    s = max(s, si + dp(i + x, max(x, m), False))
                else:
                    s = min(s, dp(i + x, max(x, m), True))
            return s
        
        return dp(0, 1, True)