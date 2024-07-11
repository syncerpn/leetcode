# so it should have at most one change 0 -> 1 or 1 -> 0
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        d = 0
        for a, b in pairwise(s):
            d += a != b
            if d >= 2:
                return False
        
        return True