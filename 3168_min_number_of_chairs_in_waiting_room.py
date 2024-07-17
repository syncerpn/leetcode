# track max count of chairs
class Solution:
    def minimumChairs(self, s: str) -> int:
        m = 0
        t = 0
        for c in s:
            if c == "E":
                t += 1
                m = max(m, t)
            else:
                t -= 1
        return m