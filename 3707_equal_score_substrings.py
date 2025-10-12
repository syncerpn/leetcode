# easy
class Solution:
    def scoreBalance(self, s: str) -> bool:
        p = sum(ord(c) - 96 for c in s)
        if p % 2:
            return False
        p //= 2
        q = 0

        for c in s:
            q += ord(c) - 96
            if q == p:
                return True
            elif q > p:
                break
        return False