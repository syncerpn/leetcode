# math
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        a, b = max(cost1, cost2), min(cost1, cost2)
        n = total // a
        ans = 0
        for i in range(n + 1):
            ans += (total - i * a) // b + 1
        return ans