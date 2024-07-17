# stack obvs
class Solution:
    def clearDigits(self, s: str) -> str:
        DIGITS = "1234567890"
        t = []
        for c in s:
            if c in DIGITS:
                t.pop()
            else:
                t.append(c)
        
        return "".join(t)