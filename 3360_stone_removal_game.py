# simulate it
class Solution:
    def canAliceWin(self, n: int) -> bool:
        a = False
        k = 10
        while n >= k:
            n -= k
            k -= 1
            a = not a
        return a