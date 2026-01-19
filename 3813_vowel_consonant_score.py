# easy
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        V = "aeiou"
        C = "bcdfghjklmnpqrstvwxyz"
        v, c = 0, 0
        for a in s:
            if a in V:
                v += 1
            elif a in C:
                c += 1
        return 0 if c == 0 else v // c