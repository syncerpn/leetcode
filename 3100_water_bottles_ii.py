# easy
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans, b, e = numBottles, numBottles, numExchange
        while b >= e:
            ans += 1
            b += -e + 1
            e += 1
        return ans