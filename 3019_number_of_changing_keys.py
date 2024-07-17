# easy
class Solution:
    def countKeyChanges(self, s: str) -> int:
        c = 0
        for a, b in pairwise(s):
            if a.lower() != b.lower():
                c += 1
        return c