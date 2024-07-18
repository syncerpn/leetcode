# math makes it beautiful
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m * m
        return (n + 1) * n // 2 - (m + k) * ((k - m) // m + 1)