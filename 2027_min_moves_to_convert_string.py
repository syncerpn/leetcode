# after a conversion, jump to the next 3
class Solution:
    def minimumMoves(self, s: str) -> int:
        r = 0
        i = 0
        while i < len(s):
            if s[i] == "X":
                r += 1
                i += 2
            i += 1
            
        return r