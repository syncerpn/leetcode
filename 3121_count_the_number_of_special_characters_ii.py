# easy
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        U = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        A, B, C = set(), set(), set()
        for c in word:
            if c in U:
                c = c.lower()
                if c not in A:
                    C.add(c)
                else:
                    B.add(c)
            else:
                if c in B:
                    C.add(c)
                else:
                    A.add(c)
        return len(B - C)