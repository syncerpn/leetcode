# easy
class Solution:
    def reverseDegree(self, s: str) -> int:
        A = {c: 26 - i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        return sum((i+1) * A[c] for i, c in enumerate(s))
