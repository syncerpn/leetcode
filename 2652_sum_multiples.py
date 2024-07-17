# brute-force should be fine
# but math makes it beautiful
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sum_n(n, d):
            k = n // d
            return k * (k + 1) * d // 2
        
        return sum_n(n, 3) + sum_n(n, 5) + sum_n(n, 7) - sum_n(n, 3*5) - sum_n(n, 3*7) - sum_n(n, 5*7) + sum_n(n, 3*5*7)