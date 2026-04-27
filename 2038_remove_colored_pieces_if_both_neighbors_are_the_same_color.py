# easy
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, A = -2, 0
        b, B = -2, 0
        for c in colors:
            if c == "A":
                a += 1
                b = -2
                if a > 0:
                    A += 1
            else:
                b += 1
                a = -2
                if b > 0:
                    B += 1
        return A > B