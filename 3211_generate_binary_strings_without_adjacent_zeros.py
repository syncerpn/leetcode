# recursion makes it simple
class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        r = []
        for s in self.validStrings(n-1):
            if s[0] == "1":
                r.append("0" + s)
            r.append("1" + s)
        return r