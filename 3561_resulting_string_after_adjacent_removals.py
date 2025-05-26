# simple stack
class Solution:
    def resultingString(self, s: str) -> str:
        d = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        r = []
        for c in s:
            if r and (abs(d[r[-1]] - d[c]) == 1 or abs(d[r[-1]] - d[c]) == 25):
                r.pop()
            else:
                r.append(c)
        
        return "".join(r)