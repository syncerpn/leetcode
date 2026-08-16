# easy
class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        m = max(lights)
        ans = 0
        for a in arrivalTime:
            a %= period
            if a >= m:
                ans = max(ans, period - a)
        return ans