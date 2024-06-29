# single-pass O(1) space
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h = 0
        v = 0
        for c in moves:
            if c == "U":
                v -= 1
            elif c == "D":
                v += 1
            elif c == "R":
                h += 1
            elif c == "L":
                h -= 1
        
        return h == 0 and v == 0