# easy
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b = 0, 1
        while n > b * 2:
            a, b = b, a + b
        return n == 2 * b