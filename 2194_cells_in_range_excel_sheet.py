# string parser + range generator
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cs = ALPHABETS.find(s[0])
        ce = ALPHABETS.find(s[3])
        rs = int(s[1])
        re = int(s[4])
        result = []
        for ci in range(cs, ce+1):
            for ri in range(rs, re+1):
                result.append(ALPHABETS[ci] + str(ri))
        
        return result