# easy
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        mi = 2
        if b - a == 1 and c - b == 1:
            mi = 0
        elif b - a <= 2 or c - b <= 2:
            mi = 1
        ma = c - a - 2
        return mi, ma