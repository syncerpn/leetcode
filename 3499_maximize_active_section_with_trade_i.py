# likely sliding window
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        x, y, z = 0, 0, 0
        n = 0
        m = 0
        for c in s:
            if c == "1":
                n += 1
                if x == 0:
                    continue
                if z > 0:
                    m = max(m, x + z)
                    x, y, z = z, 0, 0
                y += 1
            else:
                if y > 0:
                    z += 1
                else:
                    x += 1
        if z > 0:
            m = max(m, x + z)
        return n + m