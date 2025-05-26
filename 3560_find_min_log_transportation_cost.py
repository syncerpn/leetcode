# easy
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        ans = 0
        for a in [m, n]:
            if a < k:
                continue
            ans += k * (a - k)
        return ans
