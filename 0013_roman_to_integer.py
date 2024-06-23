# roman string should be sorted
# any "misplaced" char should be subtracted
class Solution:
    def romanToInt(self, s: str) -> int:
        D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = 0
        cp = ''
        for c in s:
            if cp:
                if D[cp] < D[c]:
                    n -= D[cp]
                else:
                    n += D[cp]
            cp = c
        
        n += D[cp]
        return n