# easy but quite tedious to implement
class Solution:
    def generateTag(self, caption: str) -> str:
        U, C = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Au = {u: c for u, c in zip(U + C, C + C)}
        Ac = {c: u for u, c in zip(U + U, C + U)}
        s = "#"
        ff, f = True, False
        for c in caption:
            if c == " ":
                if not ff:
                    f = True
            else:
                if ff:
                    c = Ac[c]
                    ff = False
                elif f:
                    c = Au[c]
                    f = False
                else:
                    c = Ac[c]
                s += c
            if len(s) >= 100:
                break
        return s