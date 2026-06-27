# easy
class Solution:
    def maxDistance(self, moves: str) -> int:
        h = abs(moves.count("L") - moves.count("R"))
        v = abs(moves.count("U") - moves.count("D"))
        a = moves.count("_")
        return h + v + a