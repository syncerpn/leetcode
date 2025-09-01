# nice problem
# its pure math, but had no time to do it during the contest
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        def ceil(x, y):
            return (x + y - 1) // y

        n = len(s)
        z = s.count("0")

        if n == k:
            return 0 if z == 0 else 1 if z == n else -1

        ans = inf
        if z % 2 == 0:
            m = max(ceil(z, k), ceil(z, n - k))
            m += m & 1
            ans = min(ans, m)
        if z % 2 == k % 2:
            m = max(ceil(z, k), ceil(n - z, n - k))
            m += m & 1 == 0
            ans = min(ans, m)

        return ans if ans < inf else -1
        