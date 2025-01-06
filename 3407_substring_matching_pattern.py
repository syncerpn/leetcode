# divide the pattern by *, then try to find each sub pattern greedily
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p = p.split("*")
        i = 0
        for a in p:
            j = s[i:].find(a)
            if j == -1:
                return False
            i += j + len(a)
        return True