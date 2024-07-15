# easy
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = 0
        for c in s:
            if c == letter:
                n += 1
        return n * 100 // len(s)