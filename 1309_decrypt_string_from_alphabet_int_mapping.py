# string condition checking
class Solution:
    def freqAlphabets(self, s: str) -> str:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        d = {str(ord(c)-96) + ("#" if ord(c) > 105 else ""): c for c in ALPHABET}

        i = 0
        n = len(s)
        r = ""
        while i < n:
            if i < n - 2 and s[i+2] == "#":
                r += d[s[i:i+3]]
                i += 3
            else:
                r += d[s[i]]
                i += 1
        return r