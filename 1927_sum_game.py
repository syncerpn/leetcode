# a few cases
# when alice take the last move, no way bob can win
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        d = 0
        f = 0
        
        for i, c in enumerate(num):
            if i < n // 2:
                if c == "?":
                    f += 1
                else:
                    d += int(c)
            else:
                if c == "?":
                    f -= 1
                else:
                    d -= int(c)
        if f == 0:
            return d != 0
            
        if f % 2:
            return True

        if (f > 0 and d > 0) or (f < 0 and d < 0):
            return True

        d, f = abs(d), abs(f)
        return 9 * f != 2 * d