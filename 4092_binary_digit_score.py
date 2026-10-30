# easy
class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        aa = a.bit_count()
        bb = b.bit_count()
        return aa * bb if aa >= bb else bb // aa