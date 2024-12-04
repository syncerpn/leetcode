# without math, we call form this formula
class Solution:
    d = {1:1, 2: 1/2}
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n not in Solution.d:
            Solution.d[n] = 1/n + (n-2)/n * self.nthPersonGetsNthSeat(n-1)
        return Solution.d[n]

# then math makes everything super elegant O(1)
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5