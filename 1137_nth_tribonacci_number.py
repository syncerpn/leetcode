# calculate + memoi
class Solution:
    _d = {0: 0, 1: 1, 2: 1}
    def tribonacci(self, n: int) -> int:
        if n in Solution._d:
            return Solution._d[n]
        t = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        Solution._d[n] = t
        return t