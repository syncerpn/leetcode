# set
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        r = set()
        for c in s:
            if c in r:
                return c
            r.add(c)
        return ""