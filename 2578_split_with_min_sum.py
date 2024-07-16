# alternating formation
class Solution:
    def splitNum(self, num: int) -> int:
        s = sorted(str(num))
        n = len(s)
        a = "".join([s[i] for i in range(0,n,2)])
        b = "".join([s[i] for i in range(1,n,2)])
        return int(a) + int(b)