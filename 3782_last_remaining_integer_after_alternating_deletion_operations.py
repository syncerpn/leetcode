# codeforce makes me learn math
# which helped this case lol
# simply use math to track the first and last of the sequence
class Solution:
    def lastInteger(self, n: int) -> int:
        l, r = 1, n
        d = 1
        m = True
        while l != r:
            if m:
                r = l + (r - l) // (d * 2) * (d * 2)
            else:
                l = r - (r - l) // (d * 2) * (d * 2)
            m = not m
            d <<= 1
        
        return l