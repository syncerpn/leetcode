# easy, greedy
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = 0
        a = 0
        for b in rungs:
            q, r = (b - a) // dist, (b - a) % dist
            ans += q + int(r > 0) - 1
            a = b
        return ans