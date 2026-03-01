# memoi solution
class Solution:
    def minCost(self, n: int) -> int:
        @functools.cache
        def helper(k):
            if k == 1:
                return 0

            ans = inf
            for a in range(1, k // 2 + 1):
                ans = min(ans, a * (k - a) + helper(a) + helper(k - a))
            return ans
        return helper(n)

# math did this dirty
# always split into 1 and n - 1
class Solution:
    def minCost(self, n: int) -> int:
        return n * (n - 1) // 2