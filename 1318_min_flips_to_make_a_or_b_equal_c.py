# bit check
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        n = 0
        for i in range(32):
            ai = (a >> i) & 1
            bi = (b >> i) & 1
            ci = (c >> i) & 1
            if (ai | bi) != ci:
                if ci == 1:
                    n += 1
                else:
                    n += ai + bi
        return n