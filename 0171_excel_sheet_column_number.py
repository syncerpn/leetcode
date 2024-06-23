# just use math
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        for c in columnTitle:
            n = n * 26 + (ord(c) - 64)
        return n