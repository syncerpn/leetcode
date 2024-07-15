class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c = 0
        for w in words:
            c += s.startswith(w)
        return c