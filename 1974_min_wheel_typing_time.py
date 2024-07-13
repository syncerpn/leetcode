# try to minimize travel distance to the next char
class Solution:
    def minTimeToType(self, word: str) -> int:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        AI = {c: i for i, c in enumerate(ALPHABET)}
        t = 0
        p = "a"
        for c in word:
            d = abs(AI[c] - AI[p])
            t += 1 + min(d, 26-d)
            p = c
        return t