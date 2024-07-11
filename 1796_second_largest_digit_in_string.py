# track largest and second largest on the way
class Solution:
    def secondHighest(self, s: str) -> int:
        DIGITS = "0123456789"
        a = None
        b = None
        for c in s:
            if c not in digits:
                continue
            i = int(c)
            if a is None:
                a = i
            elif a < i:
                a, b = i, a
            elif a == i:
                continue
            elif b is None:
                b = i
            elif b < i:
                b = i
        
        return -1 if b is None else b