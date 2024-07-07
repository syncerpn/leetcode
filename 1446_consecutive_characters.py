# pairwise checking
# increase length if current char == previous char
class Solution:
    def maxPower(self, s: str) -> int:
        m = 1
        d = 1
        for p, c in pairwise(s):
            if c == p:
                d += 1
                m = max(m, d)
            else:
                d = 1
        
        return m