# fairly easy
class Solution:
    def maxDiff(self, num: int) -> int:
        def replace(s, u, v):
            return [v if c == u else c for c in s]

        mi = list(str(num))
        for i, c in enumerate(mi):
            if c != "1":
                if i == 0:
                    mi = replace(mi, c, "1")
                    break
                elif c != "0":
                    mi = replace(mi, c, "0")
                    break
        
        ma = list(str(num))
        for i, c in enumerate(ma):
            if c != "9":
                ma = replace(ma, c, "9")
                break
        return int("".join(ma)) - int("".join(mi))