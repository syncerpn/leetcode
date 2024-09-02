# check whether they have the same mod-2 result
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        a, b = coordinate1
        c, d = coordinate2
        return (ord(a) + ord(b)) % 2 == (ord(c) + ord(d)) % 2