# easy
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        h = k // 2
        ans = 0
        for a in range(1, min(h+1, n+1)):
            ans += a
        if h < n:
            for a in range(k, k+n-h):
                ans += a
        return ans