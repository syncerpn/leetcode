# beautifully calculated lol
class Solution:
    def totalMoney(self, n: int) -> int:
        d = n // 7
        r = n  % 7
        return 28 * d + 7 * d * (d - 1) // 2 + (d * r + (1 + r) * r // 2)