# alternate sum as it is
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = True
        r = 0
        for c in str(n):
            r = (r + int(c)) if s else (r - int(c))
            s = not s
        return r