# simple string manip
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split("-")).upper()
        f = len(s) % k
        prefix = s[:f]
        p = [s[f+i*k:f+i*k+k] for i in range(len(s) // k)]
        if prefix:
            p = [prefix] + p
        return "-".join(p)