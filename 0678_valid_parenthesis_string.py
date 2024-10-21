# using stack
# try to pair "(" and ")"
# before using any "*"
class Solution:
    def checkValidString(self, s: str) -> bool:
        p = []
        for c in s:
            if c == "(" or c == "*":
                if not p or p[-1][0] != c:
                    p.append([c, 0])
                p[-1][1] += 1
            else:
                d = 0
                while p:
                    if p[-1][0] == "(":
                        p[-1][1] -= 1
                        if p[-1][1] == 0:
                            p.pop()
                        break
                    else:
                        d += p.pop()[1]
                else:
                    if d == 0:
                        return False
                    d -= 1
                p.append(["*", d])
        # try to pair remaining "(" and "*"
        d = 0
        while p:
            if p[-1][0] == "*":
                d += p.pop()[1]
            else:
                d -= p.pop()[1]
                if d < 0:
                    return False

        return True

# lee's optimized solution with O(1) space; here is his explanation:
# It's quite straight forward actually.
# When you met "(", you know you need one only one ")", cmin = 1 and cmax = 1.
# When you met "(*(", you know you need one/two/three ")", cmin = 1 and cmax = 3.
# The string is valid for 2 condition:
# cmax will never be negative.
# cmin is 0 at the end.
class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        for i in s:
            cmax = cmax - 1 if i == ")" else cmax + 1
            cmin = cmin + 1 if i == "(" else max(cmin - 1, 0)
            if cmax < 0: return False
        return cmin == 0