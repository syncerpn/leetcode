# easy
class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        a, b = source
        x, y = target
        if (a + b) % 2 != (x + y) % 2:
            return -1
        return 1 if a + b == x + y or abs(a - x) == abs(b - y) else 2