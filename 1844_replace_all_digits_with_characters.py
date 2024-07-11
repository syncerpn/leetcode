# use hash map just to lookup quickly
class Solution:
    def replaceDigits(self, s: str) -> str:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        d = {c: i for i, c in enumerate(ALPHABET)}
        s = [c for c in s]
        for i in range(len(s)):
            if s[i] not in d:
                s[i] = ALPHABET[d[s[i-1]] + int(s[i])]
        
        return "".join(s)
