# use set
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set([c for c in word])
        r = 0
        for c in s:
            if c.upper() in s and c.lower() in s:
                r += 1
        return r // 2