# simulate the process
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        c = n
        while n >= numExchange:
            c += n // numExchange
            n = n // numExchange + n % numExchange
        return c