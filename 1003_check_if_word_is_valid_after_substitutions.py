# easy stack
class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        for c in s:
            p.append(c)
            while len(p) >= 3 and p[-3] == "a" and p[-2] == "b" and p[-1] == "c":
                p.pop()
                p.pop()
                p.pop()
        return not p