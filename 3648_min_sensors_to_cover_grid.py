# easy
class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        k = 2 * k + 1
        return (n // k + (n % k > 0)) * (m // k + (m % k > 0))