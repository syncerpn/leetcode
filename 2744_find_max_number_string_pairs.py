# use set is good enough
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set()
        c = 0
        for w in words:
            r = w[::-1]
            if r in s:
                s.discard(r)
                c += 1
            s.add(w)
        return c