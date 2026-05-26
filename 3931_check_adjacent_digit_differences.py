# easy
class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for a, b in pairwise(s):
            if abs(int(a) - int(b)) > 2:
                return False
        return True