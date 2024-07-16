# just check
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        DIGITS = "0123456789"
        m = 0
        for s in strs:
            for c in s:
                if c not in DIGITS:
                    m = max(m, len(s))
                    break
            else:
                m = max(m, int(s))
        return m