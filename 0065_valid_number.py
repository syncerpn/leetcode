# not very difficult
# just so burdensome as many hard problems are
class Solution:
    def isNumber(self, s: str) -> bool:
        def helper(p, must_be_int=False):
            if not p:
                return False
            sign_count = p.count("+") + p.count("-")
            if sign_count > 1:
                return False
            if sign_count == 1 and p[0] != "+" and p[0] != "-":
                return False
            if sign_count > 1:
                return False
            deci_count = p.count(".")
            if deci_count > 1:
                return False
            if deci_count == 1 and must_be_int:
                return False
            if len(p) - deci_count - sign_count == 0:
                return False
            return True

        s = s.lower()
        v = "+-0123456789e."
        e = 0
        for c in s:
            if c not in v:
                return False
            e += c == "e"
        if e == 0:
            return helper(s)
        elif e == 1:
            l, r = s.split("e")
            return helper(l) and helper(r, must_be_int=True)
        return False