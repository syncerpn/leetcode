# fairly simple
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        r = s[:2]
        for c in s[2:]:
            if c != r[-1] or c != r[-2]:
                r += c
        
        return r