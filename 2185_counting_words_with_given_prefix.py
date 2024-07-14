# python makes it easy
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c = 0
        for word in words:
            if word.startswith(pref):
                c += 1
        return c