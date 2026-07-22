# easy
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        d = Counter(list(s))
        return y * d[y] + "".join([c * d[c] for c in d if (c != x and c != y)]) + x * d[x]