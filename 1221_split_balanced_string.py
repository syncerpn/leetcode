# solve the problem with balance
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        t = 0
        r = 0
        for c in s:
            if c == "R":
                t += 1
            elif c == "L":
                t -= 1
            if t == 0:
                r += 1
        
        return r