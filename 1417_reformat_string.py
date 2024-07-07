# how about stack push pop
class Solution:
    def reformat(self, s: str) -> str:
        d = []
        c = []
        for i in s:
            if i in "0123456789":
                d.append(i)
            else:
                c.append(i)

        r = ""
        if abs(len(d) - len(c)) > 1:
            return r

        while d and c:
            r += c.pop() + d.pop()
        if not d and not c:
            return r
        return r + c.pop() if c else d.pop() + r