# easy
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        k = 1
        for a, b in pairwise(prices):
            if b - a == -1:
                k += 1
            else:
                ans += k * (k + 1) // 2
                k = 1
        ans += k * (k + 1) // 2
        return ans

# or more like dp
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 1
        k = 1
        for a, b in pairwise(prices):
            if b - a == -1:
                k += 1
            else:
                k = 1
            ans += k
        return ans