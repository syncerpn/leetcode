# got it right in the first trial
# lol
class Solution:
    def decodeString(self, s: str) -> str:
        r = [""]
        m = [""]
        ans = ""
        d = ""
        for c in s:
            if c == "[":
                m.append(d)
                r.append("")
                d = ""
            elif c == "]":
                ri = r.pop()
                mi = m.pop()
                r[-1] += int(mi) * ri
            elif c.isdigit():
                d += c
            else:
                r[-1] += c
                d = ""
        
        return r[0]