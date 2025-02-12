# fairly easy
class Solution:
    def findValidPair(self, s: str) -> str:
        d = Counter(s)
        for a, b in pairwise(s):
            if a != b and int(a) == d[a] and int(b) == d[b]:
                return a + b
        return ""