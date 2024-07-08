# simple stack
class Solution:
    def makeGood(self, s: str) -> str:
        r = []
        for c in s:
            if r and c != r[-1] and c.lower() == r[-1].lower():
                r.pop()
            else:
                r.append(c)
        return "".join(r)