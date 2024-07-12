# iterate, with skipping as a small improvement, lol
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = 0
        i = 0
        while i < len(s) - 2:
            if s[i+2] == s[i+1]:
                i += 1
            elif s[i+1] != s[i] and s[i+2] != s[i]:
                c += 1
            i += 1
        
        return c