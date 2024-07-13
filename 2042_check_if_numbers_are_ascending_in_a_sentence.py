# fairly simple
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        DIGITS = "0123456789"
        d = list(map(int, [w for w in s.split(" ") if w[0] in DIGITS]))
        for a, b in pairwise(d):
            if a >= b:
                return False
        return True
