# easy
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        D = []
        L = []
        for s in logs:
            i, *c = s.split(" ")
            c = " ".join(c)
            if c[0] in "0123456789":
                D.append(s)
            else:
                L.append((c, i))
        
        L.sort()
        L = [b + " " + a for a, b in L]
        return L + D
