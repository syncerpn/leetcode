# easy
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = 0
        r = 0
        n = 0
        for c in moves:
            if c == "L":
                l += 1
            elif c == "R":
                r += 1
            elif c == "_":
                n += 1
        return max(l, r) + n - min(l, r)