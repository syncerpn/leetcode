# easy
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        z = 0 
        o = 0
        for c in s:
            if c == "0":
                z += 1
            else:
                o += 1
        return "1" * (o-1) + "0" * z + "1"