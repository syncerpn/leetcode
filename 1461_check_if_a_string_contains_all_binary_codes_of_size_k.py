# easy
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        m = (1 << k) - 1
        v = set()
        p = 0
        for i, c in enumerate(s):
            p = ((p << 1) | int(c)) & m
            if i >= k - 1:
                v.add(p)
        
        return len(v) == m + 1