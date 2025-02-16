# fairly easy
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        t = 1
        for a, b in pairwise(s):
            if b == a:
                t += 1
            elif t == k:
                return True
            else:
                t = 1
        return t == k