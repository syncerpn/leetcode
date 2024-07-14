# hash map obviously
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
        d = {c: 0 for c in ALPHABETS}
        for c in word1:
            d[c] += 1
        for c in word2:
            d[c] -= 1

        s = 0
        for c in d:
            if abs(d[c]) > 3:
                return False
        return True