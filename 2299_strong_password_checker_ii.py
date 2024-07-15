# just check
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        S = "!@#$%^&*()-+"
        D = "1234567890"
        l, u, d, s = 0, 0, 0, 0
        
        for a, b in pairwise(" " + password):
            if a == b:
                return False
            if b in S:
                s += 1
            elif b in D:
                d += 1
            elif b.lower() == b:
                l += 1
            elif b.upper() == b:
                u += 1
        
        return all([l, u, d, s])