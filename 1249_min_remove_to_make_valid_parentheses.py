# it is just stack as usual
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        r = []
        for i, c in enumerate(s):
            if c == "(":
                r.append(("(", i))
            elif c == ")":
                if r and r[-1][0] == "(":
                    r.pop()
                else:
                    r.append((")", i))
        t = ""
        p = 0
        j = 0
        while j < len(r):
            for i in range(p, r[j][1]):
                t += s[i]
            p = r[j][1] + 1
            j += 1
        
        t += s[p:]
        return t