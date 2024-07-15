# just check
class Solution:
    def greatestLetter(self, s: str) -> str:
        m = ""
        l = set()
        for c in s:
            l.add(c)
            if c.lower() in l and c.upper() in l:
                m = max(m, c.upper())
        return m
            