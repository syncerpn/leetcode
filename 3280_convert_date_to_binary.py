# easy with bin
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y, m, d = date.split("-")
        return bin(int(y))[2:] + "-" + bin(int(m))[2:] + "-" + bin(int(d))[2:]